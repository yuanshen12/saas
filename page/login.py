from common.common_auth import Auth


class Login():

    def __init__(self, driver):
        self.driver = driver

    def get_login(self, driver, login_input, passwd_input):
        auth = Auth().auth_all('./img/img_03.png')
        driver.find_elements_by_class_name("el-input__inner")[1].clear()
        driver.find_elements_by_class_name("el-input__inner")[2].clear()
        driver.find_elements_by_class_name("el-input__inner")[3].clear()
        driver.find_elements_by_class_name("el-input__inner")[1].send_keys(login_input)
        driver.find_elements_by_class_name("el-input__inner")[2].send_keys(passwd_input)
        driver.find_elements_by_class_name("el-input__inner")[3].send_keys(auth)
        driver.find_element_by_class_name("login_btn").click()