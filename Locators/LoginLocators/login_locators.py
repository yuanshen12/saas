from selenium.webdriver.common.by import By
from Common.plugs.basepage import BasePage


class LoginLocators(BasePage):

    choose_service = (By.CLASS_NAME, "el-input__inner")
    choose_156 = (By.CLASS_NAME, "el-select-dropdown__item")
    login_click = (By.CLASS_NAME, "login-btn")

    input_loc = (By.CLASS_NAME, "el-input__inner")
    login_loc = (By.CLASS_NAME, "login_btn")
    login_error = (By.CLASS_NAME, "el-form-item__error")
    login_error_pd = (By.CLASS_NAME, "mermaidTooltip")
    login_success = (By.CLASS_NAME, "welcome_name")

    # 选择156测试环境
    def get_login_click(self):
        self.click_element(self.choose_service)
        self.click_element(self.choose_156, num=0)
        self.click_element(self.login_click, num=0)

    def get_login(self, username, password, auth):
        self.input_element(self.input_loc, username, keys_control=1, num=1)
        self.input_element(self.input_loc, password, keys_control=1, num=2)
        self.input_element(self.input_loc, auth, keys_control=1, num=3)
        self.click_element(self.login_loc)

    def get_error_username(self):
        return self.get_element_text(self.login_error)

    def get_error_password(self):
        return self.get_element_text(self.login_error_pd)

    def get_error_auth(self):
        return self.get_element_text(self.login_error, num=2)

    def get_login_success(self):
        return self.get_element_text(self.login_success)
