import pytest
from common.common_auth import Auth
from TestDatas.LoginDatas import login_datas as LD
from Locators.LoginLocators.login_locators import LoginLocators
from selenium.webdriver.common.by import By
import time
from selenium import webdriver


# def login_1(test_login, login_input, passwd_input):
#     driver = test_login
#     auth = Auth().auth_all('../img/img_03.png')
#     driver.find_elements_by_class_name("el-input__inner")[1].clear()
#     driver.find_elements_by_class_name("el-input__inner")[2].clear()
#     driver.find_elements_by_class_name("el-input__inner")[3].clear()
#     driver.find_elements_by_class_name("el-input__inner")[1].send_keys(login_input)
#     driver.find_elements_by_class_name("el-input__inner")[2].send_keys(passwd_input)
#     driver.find_elements_by_class_name("el-input__inner")[3].send_keys(auth)
#     driver.find_element_by_class_name("login_btn").click()


# @pytest.mark.parametrize('login_input, passwd_input', [('13558252700', 'admin123456')])
# @pytest.mark.parametrize('data', LD.error_username_data)
# def test_login(start_module, data):
#     driver = start_module
#     auth = Auth().auth_all('../img/img_03.png')
    # driver.find_elements_by_class_name(loc.login_loc[1])[1].clear()
    # driver.find_elements_by_class_name(loc.login_loc[1])[2].clear()
    # driver.find_elements_by_class_name(loc.login_loc[1])[3].clear()
    # driver.find_elements_by_class_name("el-input__inner")[1].send_keys(data['username'])
    # driver.find_elements_by_class_name("el-input__inner")[2].send_keys(data["password"])
    # driver.find_elements_by_class_name("el-input__inner")[3].send_keys(auth)
    # driver.find_element_by_class_name("login_btn").click()
    # time.sleep(10)
    # title = driver.current_url
    # assert title == "http://192.168.0.156:8901/#/welcome"


class TestLogin():
    login_loc = (By.CLASS_NAME, "el-input__inner")

    @pytest.mark.parametrize('data', LD.error_username_data)
    def test_login(self, start_module, data):
        self.driver = start_module
        auth = Auth().auth_all('../img/img_03.png')
        print(type(self.login_loc))
        self.driver.find_elements(self.login_loc)[1].send_keys(123456789)
        time.sleep(10)
        self.driver.find_elements(self.login_loc)[2].send_keys(data["password"])
        self.driver.find_elements(self.login_loc)[3].send_keys(auth)
        # LoginLocators(self.driver).get_login(data['username'], data['password'], auth)
        # self.driver.find_element_by_class_name("login_btn").click()
        time.sleep(10)
        title = self.driver.current_url
        assert title == "http://192.168.0.156:8901/#/welcome"


if __name__ == '__main__':
    pytest.main(['-s', 'login_test.py'])
