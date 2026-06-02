import json
from django.shortcuts import render

from .crawling import fetch_visible_comments
from .preprocessing import (
    preprocess_comments,
    augment_comments,
    summarize_comments,
)
from .models import CommentResult


def index(request):
    company_name = ""

    error_message = None
    success_message = None
    status_message = None

    raw_comments = []
    cleaned_comments = []
    augmented_comments = []
    integrated_comments = []
    summary_text = ""
    iqr_info = None

    if request.method == "POST":
        company_name = request.POST.get("company_name", "").strip()

        if not company_name:
            error_message = "회사명을 입력해주세요."

        else:
            try:
                # 1. 댓글 수집
                stock_info = fetch_visible_comments(company_name, limit=20)

                # 예외 1: 회사 검색 실패 또는 예상하지 못한 반환값
                if not stock_info:
                    error_message = "회사 검색 결과를 찾을 수 없습니다. 회사명을 다시 확인해주세요."
                    status_message = "검색 결과 없음"
                else:
                    raw_comments = stock_info.get("comments", [])

                    # 예외 2: 회사는 찾았지만 댓글이 없는 경우
                    if not raw_comments:
                        error_message = (
                            "댓글 데이터가 존재하지 않습니다. "
                            "해당 회사 커뮤니티에 댓글이 없거나 현재 댓글을 불러올 수 없습니다."
                        )
                        status_message = "댓글 데이터 없음"

                    else:
                        # 2. 전처리
                        cleaned_comments, iqr_info = preprocess_comments(raw_comments)

                        # 예외 3: 전처리 후 데이터가 모두 제거된 경우
                        if not cleaned_comments:
                            status_message = (
                                "전처리 결과 사용 가능한 댓글이 없습니다. "
                                "원본 댓글은 수집되었지만, 불필요한 패턴 또는 이상치로 제거되었습니다."
                            )
                            augmented_comments = []
                            summary_text = summarize_comments(raw_comments)

                        else:
                            # 3. 증강
                            augmented_comments = augment_comments(cleaned_comments)

                            # 4. 요약
                            # 전체 수집 댓글 기준으로 주요 내용 요약
                            summary_text = summarize_comments(raw_comments)

                            status_message = "댓글 수집, 전처리, 증강, 요약이 완료되었습니다."

                        # 5. 최종 통합 데이터
                        # 최종 결과는 전처리 데이터 + 증강 데이터
                        integrated_comments = []

                        for comment in cleaned_comments:
                            integrated_comments.append({
                                "stage": "전처리",
                                "comment": comment,
                            })

                        for comment in augmented_comments:
                            integrated_comments.append({
                                "stage": "증강",
                                "comment": comment,
                            })

                        # 6. DB 저장
                        CommentResult.objects.create(
                            company_name=company_name,
                            raw_comments="\n".join(raw_comments),
                            cleaned_comments="\n".join(cleaned_comments),
                            augmented_comments="\n".join(augmented_comments),
                            iqr_info=json.dumps(iqr_info, ensure_ascii=False),
                        )

                        success_message = (
                            f"원본 {len(raw_comments)}개, "
                            f"전처리 {len(cleaned_comments)}개, "
                            f"증강 {len(augmented_comments)}개, "
                            f"최종 결과 {len(integrated_comments)}개 생성 완료"
                        )

            except Exception as e:
                error_message = (
                    "처리 중 오류가 발생했습니다. "
                    "회사명이 올바른지 확인하거나 잠시 후 다시 시도해주세요."
                )
                status_message = f"오류 상세: {e}"

    context = {
        "company_name": company_name,
        "error_message": error_message,
        "success_message": success_message,
        "status_message": status_message,
        "raw_comments": raw_comments,
        "cleaned_comments": cleaned_comments,
        "augmented_comments": augmented_comments,
        "integrated_comments": integrated_comments,
        "summary_text": summary_text,
        "iqr_info": iqr_info,
    }

    return render(request, "comments/index.html", context)