from selenium.webdriver.common.by import By


class LoginLocators():

    def __init__(self, driver):
        self.driver = driver

    login_loc = (By.CLASS_NAME, "el-input__inner")

    def get_login(self, username, password, auth):
        print(self.login_loc)
        self.driver.find_elements(self.login_loc)[1].send_keys(username)
        self.driver.find_elements(self.login_loc)[2].send_keys(password)
        self.driver.find_elements(self.login_loc)[3].send_keys(auth)
