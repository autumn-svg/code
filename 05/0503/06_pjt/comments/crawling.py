import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

try:
    from webdriver_manager.chrome import ChromeDriverManager
except Exception:
    ChromeDriverManager = None


BASE_DIR = Path(__file__).resolve().parent.parent
TOSS_URL = "https://www.tossinvest.com/"
LOCAL_CHROME_DRIVER = BASE_DIR / "chromedriver-win64" / "chromedriver.exe"


def create_driver():
    """080_toss_practice.py 방식처럼 ChromeDriver를 생성한다."""
    if LOCAL_CHROME_DRIVER.exists():
        service = Service(str(LOCAL_CHROME_DRIVER))
    elif ChromeDriverManager is not None:
        service = Service(ChromeDriverManager().install())
    else:
        service = Service()

    return webdriver.Chrome(service=service)


def fetch_visible_comments(company_name, limit=20, max_scroll=10):
    """
    토스증권에서 회사명 검색 -> 커뮤니티 페이지 이동 -> 화면에 보이는 댓글 텍스트 수집.

    080_toss_practice.py의 동작 흐름을 Django 프로젝트에 맞게 옮긴 함수다.
    반환값은 views.py에서 바로 사용하기 쉽도록 dict 형태로 구성한다.
    """
    driver = create_driver()

    try:
        driver.get(TOSS_URL)
        time.sleep(1)

        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys("/")
        time.sleep(1)

        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='검색어를 입력해주세요']")
            )
        )
        search_input.clear()
        search_input.send_keys(company_name)
        search_input.send_keys(Keys.ENTER)
        time.sleep(1)

        # 080_toss_practice.py에서는 /order 진입을 기다린다.
        # 토스 페이지 상태에 따라 /stocks만 보일 수도 있어 둘 중 하나를 허용한다.
        WebDriverWait(driver, 15).until(
            lambda d: "/stocks/" in d.current_url
        )

        current_url = driver.current_url
        url_parts = current_url.split("/")
        stock_code = url_parts[url_parts.index("stocks") + 1]

        community_url = f"https://www.tossinvest.com/stocks/{stock_code}/community"
        driver.get(community_url)
        time.sleep(1)

        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#stock-content"))
            )
        except Exception:
            pass

        time.sleep(2)

        comments = []
        last_height = driver.execute_script("return document.body.scrollHeight")

        # 080_toss_practice.py에서 사용한 댓글 후보 selector.
        # 첫 번째 selector가 실제 댓글 본문에 가장 가깝다.
        comment_selectors = [
            "div > div.tc3tm81 > div > div.tc3tm85 > span > span",
            "article.comment span",
            "#stock-content article span",
        ]

        for _ in range(max_scroll):
            spans = []

            for selector in comment_selectors:
                spans = driver.find_elements(By.CSS_SELECTOR, selector)
                if spans:
                    break

            for span in spans:
                text = span.text.strip()

                if not text:
                    continue

                if text in comments:
                    continue

                comments.append(text)

                if len(comments) >= limit:
                    break

            if len(comments) >= limit:
                break

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break

            last_height = new_height

        return {
            "input_company": company_name,
            "stock_code": stock_code,
            "stock_url": current_url,
            "community_url": community_url,
            "comments": comments[:limit],
            "comment_count": len(comments[:limit]),
        }

    finally:
        driver.quit()


# 기존 views.py 또는 다른 파일에서 fetch_community_comments를 import하더라도 동작하도록 별칭 제공
def fetch_community_comments(company_name, limit=20, max_scroll=10):
    return fetch_visible_comments(company_name, limit=limit, max_scroll=max_scroll)
