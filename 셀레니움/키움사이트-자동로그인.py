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
from selenium.webdriver.support.ui import Select
import pandas as pd


# https://aday7.tistory.com/entry/Python-Selenium%EC%9C%BC%EB%A1%9C-%EB%84%A4%EC%9D%B4%EB%B2%84-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EC%9E%90%EB%8F%99%ED%99%94-%EB%B3%B4%EC%95%88-%EC%BA%A1%EC%B1%A0-%ED%9A%8C%ED%94%BC-%EB%B0%A9%EB%B2%95?category=1076066

class KioomSiteLoginService():

    def __init__(self):
        self.isLogin = False
        self.driver = None

    def open_web_mode(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        # self.driver = webdriver.Chrome(options=chrome_options)
        self.driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
        self.driver.set_page_load_timeout(10)

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    # https: // m.blog.naver.com / o12486vs2 / 221917465949
    def login(self):
        try:
            # test_id = "n3316202"
            # test_passwd = "nn6729"
            test_passwd = "##nn6729##"

            self.driver.get("https://www1.kiwoom.com/h/loginView?dummyVal=0")
            # self.driver.get("https://www1.kiwoom.com/h/main")
            time.sleep(5)  # 페이지 로딩 대기

            self.check_iframe()

            # 공인인증서 이동
            # login_button = self.driver.find_element(By.CSS_SELECTOR, "#header-inner > div.gnb-area > button")
            # print(login_button.text)
            # login_button.click()
            # time.sleep(10)

            # 공인인증서 이동
            cert_button = self.driver.find_element(By.ID, "onlyCert")
            cert_button.click()
            time.sleep(5)

            # iframe 이동
            iframe = self.driver.find_element(By.ID, 'yettie_iframe')
            self.driver.switch_to.frame(iframe)

            # 공인인증서 패스워드 입력
            pw_input = self.driver.find_element(By.ID, "passwordInput")
            pw_input.click()

            pyperclip.copy(test_passwd)
            actions = ActionChains(self.driver)
            actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
            time.sleep(1)  # 입력 후 잠시 대기

            # 로그인 버튼 클릭
            self.driver.find_element(By.ID, "submit_btn").click()
            self.isLogin = True
        except:
            self.isLogin = False
            print("로그인 중 에러가 발생하였습니다.")

    def remove_popup(self):
        print(self.driver.current_url)
        main = self.driver.window_handles
        print(main)
        # self.driver.get("https://www1.kiwoom.com/h/loginView?dummyVal=0")
        self.driver.get(self.driver.current_url)
        time.sleep(3)

        href_elements = self.driver.find_element(By.XPATH, '//a[@href]')

        for elem in href_elements:
            print(elem.get_attribute("href"))

    def check_iframe(self):
        iframes = self.driver.find_element(By.TAG_NAME, "iframe")
        print(iframes)

    # 외화 환전
    # https://www1.kiwoom.com/h/banking/transfer/VExchangeApplyView?dummyVal=0
    def chang_won(self, curreny, 환전구분, 환전금액):
        self.driver.get("https://www1.kiwoom.com/h/banking/transfer/VExchangeApplyView?dummyVal=0")
        time.sleep(2)

        select_element = self.driver.find_element(By.ID, 'acnt_no')
        select = Select(select_element)

        for option in select.options:
            print(option.text, end=" ")
            if option.text.find("위탁종합") != -1:
                select.select_by_visible_text(option.text)

        input_pw = self.driver.find_element(By.ID, 'pswd')
        # self.driver.execute_script('arguments[0].removeAttribute("readonly")', input_pw)
        self.driver.execute_script('document.getElementsByName("pswd")[0].removeAttribute("readonly")')

        input_pw.click()
        time.sleep(2)

        # key down
        ActionChains(self.driver) \
            .send_keys("6729") \
            .perform()

        time.sleep(1)  # 입력 후 잠시 대기

        # 조회 버튼 클릭
        self.driver.find_element(By.ID, 'btnSearch').click()

        time.sleep(1)

        if 환전구분 == 1:  # 원화 -> JPY

            select_element = self.driver.find_element(By.ID, 'crnc_code')
            select = Select(select_element)
            # USD, JPY
            select.select_by_value(curreny)

            price_won_element = self.driver.find_element(By.ID, 'exmn_able_amt')
            price_won_element.click()
            time.sleep(1)

            # key down
            ActionChains(self.driver) \
                .send_keys(str(환전금액)) \
                .perform()

            time.sleep(1)

            exchange_button = self.driver.find_element(By.ID, 'btnReg')
            exchange_button.click()

            time.sleep(2)

            exchange_detail = self.driver.find_element(By.ID, 'dialog-section-201')
            exchange_detail.screenshot('aaa.png')

            time.sleep(1)
            # 취소버튼
            cancel_button = self.driver.find_element(By.ID, 'canclebtn')
            cancel_button.click()

            # 확인버튼
            # confirm_button = self.driver.find_element(By.ID, 'confirmbtn')
            # confirm_button.click()

        else:  # JPY -> 원화
            # 옵션버튼 클릭(label을 클릭 하여야함)

            option_element = self.driver.find_element(By.XPATH,
                                                      '//*[@id="sectionContents"]/div/form/section[2]/div[2]/table/tbody/tr[1]/td/div[2]/span[1]/label')
            option_element.click()

            select_element = self.driver.find_element(By.ID, 'crnc_code2')
            select = Select(select_element)
            # USD, JPY
            select.select_by_value(curreny)

        # https: // www1.kiwoom.com / h / banking / transfer / VExchangeDayRateView
        # 일자별 환율 조회
        # def get_curreny(self,code):

    def get_currency(self, date, curreny):

        self.driver.get("https://www1.kiwoom.com/h/banking/transfer/VExchangeDayRateView")
        time.sleep(2)

        date_element = self.driver.find_element(By.ID, 'dt')
        date_element.click()

        time.sleep(1)

        delete_element = self.driver.find_element(By.XPATH,
                                                  '//*[@id="sectionContents"]/div/div[2]/div/div/div[1]/div/div/span/button[1]')
        delete_element.click()
        time.sleep(2)

        date_element.send_keys("value", date);
        print(date_element.get_attribute('value'))

        select_element = self.driver.find_element(By.ID, 'crnc_code')
        select = Select(select_element)
        # USD, JPY
        select.select_by_value(curreny)

        time.sleep(1)

        # 조회창 클릭
        self.driver.find_element(By.ID, 'btnSearch').click()

        table = self.driver.find_element(By.TAG_NAME, 'table')
        df = pd.read_html(table.get_attribute('outerHTML'))[0]
        # 더보기가 있으면 다 내리기
        while True:
            try:
                more_element = self.driver.find_element(By.CSS_SELECTOR, '#kwGridTable > div.list-more-wrap > button')
                ActionChains(self.driver).click(more_element).perform()

                table = self.driver.find_element(By.TAG_NAME, 'table')
                df = pd.read_html(table.get_attribute('outerHTML'))[0]

                time.sleep(2)
            except:
                result_element = self.driver.find_element(By.ID, 'resultMsg')
                print("실행됨")

                if result_element.text in "연속자료가 존재합니다.":
                    print("실행됨")
                    continue
                else:
                    break

        result_element = self.driver.find_element(By.ID, 'resultMsg')

        if "관련" in result_element.text:
            pass
        else:
            table = self.driver.find_element(By.TAG_NAME, 'table')
            df = pd.read_html(table.get_attribute('outerHTML'))[0]

        # tbody = table.find_element(By.TAG_NAME, "tbody")

        # columns = tbody.find_element(By.TAG_NAME, "thead")
        # rows = tbody.find_elements(By.TAG_NAME, "tr")
        # for index, value in enumerate(rows):
        #    body = value.find_elements(By.TAG_NAME, "td")[0]
        #    print(body.text)

        from datetime import datetime
        now = datetime.now()

        df.to_csv(
            now.strftime(curreny + '-' + date_element.get_attribute('value') + "-" + '%Y-%m-%d-%H-%M-%S' + '.csv'),
            index=False)

    def show_currency(self, file_name, date, curreny):
        import matplotlib.pyplot as plt
        import matplotlib.dates as mdates

        df = pd.read_csv(file_name)

        df.rename(columns={'환전율 구분': '환전율'}, inplace=True)
        df = df[df.환전율 != "가환율"]

        df['시간'] = pd.to_datetime(df['시간'], format='%H:%M:%S', errors='raise')
        df['시간_그래프용'] = df['시간'].dt.time

        print(df["시간_그래프용"])

        df = df.sort_index(ascending=False)
        print(df)

        print(df['매매기준율'].max())
        print(df['매매기준율'].min())

        div = df['매매기준율'].max() - df['매매기준율'].min()

        print(df.loc[df["매매기준율"].idxmax()]['매매기준율'])
        print(df.loc[df["매매기준율"].idxmin()])

        fig, ax = plt.subplots(figsize=(10, 7))

        ax.plot(df.loc[df["매매기준율"].idxmax()]['시간'], df.loc[df["매매기준율"].idxmax()]['매매기준율'], 'o',
                label=df.loc[df["매매기준율"].idxmax()]['시간'].strftime('%I:%M:%S') + ' ' + str(df.loc[df["매매기준율"].idxmax()]['매매기준율']), ms=10)

        ax.plot(df.loc[df["매매기준율"].idxmin()]['시간'], df.loc[df["매매기준율"].idxmin()]['매매기준율'], 'p',
                label=df.loc[df["매매기준율"].idxmin()]['시간'].strftime('%I:%M:%S') + ' ' + str(df.loc[df["매매기준율"].idxmin()]['매매기준율']), ms=10)

        ax.plot(df['시간'], df['매매기준율'], label=str(div))
        dateFmt = mdates.DateFormatter('%H:%M')
        ax.xaxis.set_major_formatter(dateFmt)
        plt.xticks(rotation=45)

        plt.legend(loc='lower right')

        plt.grid()
        plt.show()

    def update_currency(self, curreny, update_time, balance, benefit):
        # https://www1.kiwoom.com/h/banking/transfer/VExchangeDayRateView?dummyVal=0

        self.driver.get("https://www1.kiwoom.com/h/banking/transfer/VExchangeDayRateView")
        time.sleep(2)

        select_element = self.driver.find_element(By.ID, 'crnc_code')
        select = Select(select_element)

        # USD, JPY
        select.select_by_value(curreny)
        time.sleep(1)

        while True:
            try:
                # 조회창 클릭
                self.driver.find_element(By.ID, 'btnSearch').click()

                time.sleep(update_time)

                table = self.driver.find_element(By.TAG_NAME, 'table')
                df = pd.read_html(table.get_attribute('outerHTML'))[0]

                # print(df["매매기준율"][0])

                base_price = float(df["매매기준율"][0])
                buy_price = float(df["매수"][0])
                sell_price = float(df["매도"][0])

                수수료_팔때 = (base_price - sell_price) * benefit
                수수료_살때 = (buy_price - base_price) * benefit

                print("매매기준율" + str(df["매매기준율"][0]), "살때:" + str(base_price + 수수료_살때), "팔때:" + str(base_price - 수수료_팔때))

                import playsound

                목표가 = balance - (base_price + 수수료_살때)

                print("목표가" + str(목표가))

                if abs(목표가) >= 4.0:
                    print("갭발생")
                    playsound.playsound('bgsound.mp3')

            except:
                print("에러발생")
                time.sleep(5)


if __name__ == "__main__":
    kiwoom_service = KioomSiteLoginService()

    kiwoom_service.open_web_mode()
    kiwoom_service.login()
    time.sleep(1)

    # kiwoom_service.get_currency("2023.12.28", "JPY")

    #
    # #kiwoom_service.check_iframe()
    #

    # kiwoom_service.remove_popup()
    # kiwoom_service.chang_won("JPY", 1,100)

    # kiwoom_service.update_currency("JPY", 10, 912.79, 0.08)
    kiwoom_service.show_currency("JPY-2023.12.28-2023-12-28-21-50-33.csv", "", "")
