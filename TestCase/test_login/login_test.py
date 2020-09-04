import pytest
from common.common_auth import Auth
import time
from page.login import Login
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


@pytest.mark.parametrize('login_input, passwd_input', [('13558252700', 'admin123456')])
def test_login(login, login_input, passwd_input):
    driver = login
    auth = Auth().auth_all('../img/img_03.png')
    driver.find_elements_by_class_name("el-input__inner")[1].clear()
    driver.find_elements_by_class_name("el-input__inner")[2].clear()
    driver.find_elements_by_class_name("el-input__inner")[3].clear()
    driver.find_elements_by_class_name("el-input__inner")[1].send_keys(login_input)
    driver.find_elements_by_class_name("el-input__inner")[2].send_keys(passwd_input)
    driver.find_elements_by_class_name("el-input__inner")[3].send_keys(auth)
    driver.find_element_by_class_name("login_btn").click()
    time.sleep(2)
    title = driver.current_url
    assert title == "http://192.168.0.156:8901/#/welcome"


if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])
