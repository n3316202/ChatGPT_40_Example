import time
import pyperclip
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


#https://aday7.tistory.com/entry/Python-Selenium%EC%9C%BC%EB%A1%9C-%EB%84%A4%EC%9D%B4%EB%B2%84-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EC%9E%90%EB%8F%99%ED%99%94-%EB%B3%B4%EC%95%88-%EC%BA%A1%EC%B1%A0-%ED%9A%8C%ED%94%BC-%EB%B0%A9%EB%B2%95?category=1076066

class NaverLoginService():

    def __init__(self):
        self.driver = None

    def open_web_mode(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        #self.driver = webdriver.Chrome(options=chrome_options)
        self.driver = webdriver.Chrome(options=chrome_options,service=ChromeService(ChromeDriverManager().install()))
        self.driver.set_page_load_timeout(10)

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    def login(self):
        self.driver.get("https://nid.naver.com/nidlogin.login")
        time.sleep(2)  # 페이지 로딩 대기

        test_id = "nqwrt"
        test_passwd = "@@nn6729@@"

        # 아이디 입력
        id_input = self.driver.find_element(By.ID, "id")
        id_input.click()
        pyperclip.copy(test_id)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(1)  # 입력 후 잠시 대기

        # 패스워드 입력
        pw_input = self.driver.find_element(By.ID, "pw")
        pw_input.click()
        pyperclip.copy(test_passwd)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(1)  # 입력 후 잠시 대기

        # 로그인 버튼 클릭
        self.driver.find_element(By.ID, "log.login").click()

        #로그인 후 '새로운 환경' 알림에서 '등록안함' 버튼 클릭
        # try:
        #     element = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.CSS_SELECTOR, "span.btn_cancel"))
        #     )
        #     element.click()
        # except:
        #     print("기기 등록 '등록안함' 버튼을 찾을 수 없습니다.")


if __name__ == "__main__":
    naver_service = NaverLoginService()
    naver_service.open_web_mode()
    naver_service.login()
    time.sleep(5)
    #naver_service.close_browser()