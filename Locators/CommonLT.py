from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class CommonLocators(BasePage):

    choose_service = (By.CLASS_NAME, "el-input__inner")
    choose_test = (By.CLASS_NAME, "el-select-dropdown__item")
    login_click = (By.CLASS_NAME, "login-btn")

    input_loc = (By.CLASS_NAME, "el-input__inner")
    login_loc = (By.CLASS_NAME, "login_btn")

    click_subscribe = (By.CLASS_NAME, "card_wrap_icon")
    click_system = (By.CLASS_NAME, "el-menu-item")

    def get_login_click(self):
        """
        :return: 选择测试环境
        """
        self.click_element(self.choose_service)
        self.click_element(self.choose_test, num=0)
        self.click_element(self.login_click, num=0)

    def get_login(self, username, password, auth):
        """
        :param username: 登录账号
        :param password: 登录密码
        :param auth: 验证码
        :return: 正常登录账号
        """
        self.input_element(self.input_loc, username, keys_control=1, num=1)
        self.input_element(self.input_loc, password, keys_control=1, num=2)
        self.input_element(self.input_loc, auth, keys_control=1, num=3)
        self.click_element(self.login_loc)
        self.click_element(self.click_subscribe)
