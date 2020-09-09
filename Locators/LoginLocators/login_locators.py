from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginLocators():

    def __init__(self, driver):
        self.driver = driver

    choose_service = (By.CLASS_NAME, "el-input__inner")
    choose_156 = (By.CLASS_NAME, "el-select-dropdown__item")
    login_click = (By.CLASS_NAME, "login-btn")

    input_loc = (By.CLASS_NAME, "el-input__inner")
    login_loc = (By.CLASS_NAME, "login_btn")
    login_error = (By.CLASS_NAME, "el-form-item__error")
    login_success = (By.CLASS_NAME, "welcome_name")

    def get_login_click(self):
        self.driver.find_element(*self.choose_service).click()
        self.driver.find_elements(*self.choose_156)[0].click()
        self.driver.find_elements(*self.login_click)[0].click()

    def get_login(self, username, password, auth):
        element_username = self.driver.find_elements(*self.input_loc)[1]
        element_password = self.driver.find_elements(*self.input_loc)[2]
        element_auth = self.driver.find_elements(*self.input_loc)[3]
        element_username.send_keys(Keys.CONTROL, "a")
        element_username.send_keys(username)
        element_password.send_keys(Keys.CONTROL, "a")
        element_password.send_keys(password)
        element_auth.send_keys(Keys.CONTROL, "a")
        element_auth.send_keys(auth)
        self.driver.find_element(*self.login_loc).click()

    def get_error_username(self):
        error_text = self.driver.find_element(*self.login_error).text
        return error_text

    def get_error_password(self):
        error_text = self.driver.find_elements(*self.login_error)[1].text
        return error_text

    def get_error_auth(self):
        error_text = self.driver.find_elements(*self.login_error)[2].text
        return error_text

    def get_login_success(self):
        login_text = self.driver.find_element(*self.login_success).text
        return login_text
