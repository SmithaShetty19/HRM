from hrmhelper.selenium_helper import Selenium_Helper
from selenium.webdriver.common.by import By

class LoginPage(Selenium_Helper):

    email_ele = (By.ID, "user-name")
    password_ele = (By.ID, "password")
    login_ele = (By.ID, "login-button")


    def __init__(self,driver):
        super().__init__(driver)

    def login(self, username, password):
        self.webelement_enter(self.email_ele, username)
        self.webelement_enter(self.password_ele, password)
        self.webelement_click(self.login_ele)



