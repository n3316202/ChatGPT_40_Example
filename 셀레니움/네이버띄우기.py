#pip install selenium # 셀레니움 모듈 설치
#pip install --upgrade pip # pip 최신버전 업그레이드
#pip install --upgrade selenium # 셀레니움 모듈 최신버전 업그레이드
#pip install webdriver_manager # 웹드라이버 매니저 설치
#출처: https://rimeestore.tistory.com/entry/웹스크래핑-Selenium셀레니움-셋업 [리미창고:티스토리]


# 크롬 드라이버 기본 모듈
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

import time
import pyperclip

# 크롬 드라이버 자동 업데이트을 위한 모듈
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 삭제
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
# 크롬 드라이버 최신 버전 설정
service = Service(executable_path=ChromeDriverManager().install())



driver = webdriver.Chrome(service=service, options=chrome_options)
driver.set_page_load_timeout(10)

# 웹페이지 해당 주소 이동
driver.get("https://nid.naver.com/nidlogin.login")
time.sleep(2)  # 페이지 로딩 대기

test_id = "nqwrt"
test_passwd = "@@nn6729@@"

# 아이디 입력
id_input = driver.find_element(By.ID, "id")
id_input.click()
pyperclip.copy(test_id)
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
time.sleep(1)  # 입력 후 잠시 대기

# 패스워드 입력
pw_input = driver.find_element(By.ID, "pw")
pw_input.click()
pyperclip.copy(test_passwd)
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
time.sleep(1)  # 입력 후 잠시 대기

# 로그인 버튼 클릭
driver.find_element(By.ID, "log.login").click()