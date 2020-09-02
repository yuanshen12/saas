import pytest
from selenium import webdriver
from time import sleep
from PIL import Image, ImageEnhance
from common.common_auth import Auth


@pytest.fixture
def saas_login():
    driver = webdriver.Chrome("../software/chromedriver.exe")
    url = "http://192.168.0.156:8901"
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.find_element_by_class_name("el-input__inner").click()
    driver.find_elements_by_class_name("el-select-dropdown__item")[0].click()
    driver.find_elements_by_class_name("login-btn")[0].click()
    sleep(2)
    driver.find_elements_by_class_name("el-input__inner")[1].send_keys(13558252700)
    driver.find_elements_by_class_name("el-input__inner")[2].send_keys('admin123456')

    Auth(driver).auth_all('./img/')