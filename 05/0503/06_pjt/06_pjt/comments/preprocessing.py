import ast
import json
import os
import re

import pandas as pd
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


load_dotenv()


def run_llm(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("MODEL", "gpt-4o-mini")

    if not api_key:
        raise ValueError("OPENAI_API_KEY가 설정되어 있지 않습니다.")

    llm = init_chat_model(
        model,
        model_provider="openai",
        api_key=api_key,
    )

    result = llm.invoke(
        [
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )

    return result.content


def filter_inappropriate(comments):
    if not comments:
        return [], []

    numbered = "\n".join(
        f"{idx}. {comment}" for idx, comment in enumerate(comments)
    )

    prompt = f"""
다음 댓글 목록에서 부적절한 댓글의 번호만 반환해줘.

부적절 댓글 기준:
- 욕설
- 혐오
- 비방
- 선정성
- 과도한 비난
- 공격적인 표현

응답은 반드시 JSON 배열만 반환해.
예시: [0, 2, 5]
부적절 댓글이 없으면 [] 만 반환해.

댓글 목록:
{numbered}
"""

    try:
        response = run_llm(prompt).strip()
        remove_indexes = json.loads(response)
    except Exception:
        remove_indexes = []

    remove_indexes = sorted(
        set(
            int(idx)
            for idx in remove_indexes
            if isinstance(idx, (int, float)) and 0 <= int(idx) < len(comments)
        )
    )

    filtered_comments = [
        comment
        for idx, comment in enumerate(comments)
        if idx not in remove_indexes
    ]

    removed_comments = [
        comments[idx]
        for idx in remove_indexes
    ]

    return filtered_comments, removed_comments


def clean_with_pandas(comments):
    df = pd.DataFrame(comments, columns=["comment"])

    df = df.dropna(subset=["comment"])
    df["comment"] = df["comment"].astype(str).str.strip()
    df = df[df["comment"] != ""]

    df["clean"] = df["comment"].apply(
        lambda text: re.sub(r"[^가-힣a-zA-Z0-9\s]", "", text)
    )
    df["clean"] = df["clean"].str.replace(r"\s+", " ", regex=True).str.strip()

    cond_numeric = df["clean"].str.match(r"^\d+$")
    cond_repeat = df["clean"].str.match(r"^[ㅋㅎㅠㅜ]+$")
    cond_english = df["clean"].str.match(r"^[A-Za-z\s]+$")
    cond_none = df["clean"].str.lower() == "none"
    cond_short = df["clean"].str.len() < 3

    cond_any = cond_numeric | cond_repeat | cond_english | cond_none | cond_short

    removed_by_pattern = df[cond_any]["comment"].tolist()
    df = df[~cond_any]

    df["length"] = df["clean"].str.len()

    iqr_info = {
        "removed_by_pattern": removed_by_pattern,
        "removed_by_iqr": [],
        "removed_inappropriate": [],
        "q1": None,
        "q3": None,
        "iqr": None,
        "lower": None,
        "upper": None,
    }

    if len(df) >= 5:
        q1 = df["length"].quantile(0.25)
        q3 = df["length"].quantile(0.75)
        iqr = q3 - q1

        lower = max(5, q1 - 1.5 * iqr)
        upper = q3 + 1.5 * iqr

        cond_iqr = (df["length"] < lower) | (df["length"] > upper)

        iqr_info["removed_by_iqr"] = df[cond_iqr]["comment"].tolist()
        iqr_info["q1"] = q1
        iqr_info["q3"] = q3
        iqr_info["iqr"] = iqr
        iqr_info["lower"] = lower
        iqr_info["upper"] = upper

        df = df[~cond_iqr]

    cleaned_comments = df["clean"].tolist()

    return cleaned_comments, iqr_info


def augment_comments(cleaned_comments):
    if not cleaned_comments:
        return []

    prompt = f"""
다음 댓글 리스트의 의미를 유지하면서 각각 자연스럽게 다르게 표현해줘.

조건:
- 원래 의미는 유지할 것
- 투자 댓글처럼 자연스럽게 표현할 것
- 입력 댓글 개수와 동일한 개수로 만들 것
- 반드시 파이썬 리스트 형식으로만 반환할 것
- 설명, 마크다운, 코드블록은 쓰지 말 것

댓글 리스트:
{cleaned_comments}
"""

    try:
        response = run_llm(prompt).strip()
        augmented = ast.literal_eval(response)

        if not isinstance(augmented, list):
            return []

        return [
            str(comment).strip()
            for comment in augmented
            if str(comment).strip()
        ]

    except Exception:
        return []


def summarize_comments(comments):
    """
    F110: 수집된 전체 댓글 데이터를 기반으로 주요 내용 요약
    """

    if not comments:
        return "요약할 댓글 데이터가 없습니다."

    comment_text = "\n".join(
        f"{idx + 1}. {comment}" for idx, comment in enumerate(comments)
    )

    prompt = f"""
아래는 주식 커뮤니티에서 수집한 댓글 목록이야.
전체 댓글의 주요 내용을 한국어로 요약해줘.

요약 조건:
- 핵심 분위기 1문장
- 주요 의견 3가지
- 투자 판단이 아니라 댓글 데이터의 경향만 설명
- 과장하지 말 것
- 보기 좋게 줄바꿈해서 출력

댓글 목록:
{comment_text}
"""

    try:
        return run_llm(prompt).strip()
    except Exception:
        return "요약 생성 중 오류가 발생했습니다."


def preprocess_comments(raw_comments):
    filtered_comments, removed_inappropriate = filter_inappropriate(raw_comments)

    cleaned_comments, iqr_info = clean_with_pandas(filtered_comments)

    iqr_info["removed_inappropriate"] = removed_inappropriate

    return cleaned_comments, iqr_info