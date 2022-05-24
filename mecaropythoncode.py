from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select


#CityProvince = "경기도"  # 시/도
#SchoolLevel = "고등학교"  # 학교급
#SchoolName = "한봄고등학교"  # 학교 이름
#UserName = "박정원"  # 이름
#BirthDate = "041027"  # 생년월일
#Password = "1234"  # 비밀번호


class selfdiaconsis():
    def __init__(self, CityProvince, SchoolLevel, SchoolName, UserName, BirthDate, Password):
        self.CityProvince = CityProvince
        self.SchoolLevel = SchoolLevel
        self.SchoolName = SchoolName
        self.UserName = UserName
        self.BirthDate = BirthDate
        self.Password = Password

    def test(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('window-size=1920,1080')

        driver = webdriver.Chrome('./chromedriver', options=options)

        driver.get('https://hcs.eduro.go.kr')

        sleep(0.5)

        try:
            driver.find_element_by_id('password').click()
        except:
            driver.find_element_by_id('btnConfirm2').click()

            # 개인정보 입력 화면
            sleep(0.5)
            driver.find_element_by_id('schul_name_input').click()

            # 학교 관련 정보 입력 화면
            sleep(0.5)
            Select(driver.find_element_by_id('sidolabel')).select_by_visible_text(self.CityProvince)
            sleep(0.5)
            Select(driver.find_element_by_id('crseScCode')).select_by_visible_text(self.SchoolLevel)
            sleep(0.5)
            driver.find_element_by_id('orgname').send_keys(self.SchoolName)
            sleep(0.5)
            driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
            sleep(1.5)
            driver.find_element_by_css_selector(
                "#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > ul").click()
            sleep(0.5)
            driver.find_element_by_class_name('layerFullBtn').click()

            # 학교 관련 정보 입력 화면 닫음
            sleep(0.5)
            driver.find_element_by_id('user_name_input').send_keys(self.UserName)
            sleep(0.5)
            driver.find_element_by_id('birthday_input').send_keys(self.BirthDate)
            sleep(0.5)
            driver.find_element_by_id('btnConfirm').click()

            # 비밀번호 입력 화면
            sleep(0.5)
            driver.find_element_by_id('password').click()

        for i in self.Password:
            sleep(0.5)
            driver.find_element_by_css_selector(f'[aria-label="{i}"]').click()
        sleep(0.5)
        driver.find_element_by_id('btnConfirm').click()

        # 사용자 계정 선택 화면
        sleep(1.5)
        driver.find_element_by_xpath(f"//*[contains(text(), '{self.UserName}')]").click()

        # 질문 응답 화면
        for i in range(1, 4):
            sleep(0.5)
            driver.find_element_by_css_selector(
                f"#container > div.subpage > div > div:nth-child(2) > div.survey_question > dl:nth-child({i}) > dd > ul > li:nth-child(1) > label").click()
        driver.find_element_by_id('btnConfirm').click()

        print("자가진단을 완료했습니다")
        driver.close()