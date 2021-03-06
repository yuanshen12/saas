from selenium import webdriver
import pytest
import os
from TestCase.lab_test import lab_datas as LD
from Locators.CommonLT import CommonLocators as loc
from Common.common_auth import Auth

driver = None
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


@pytest.fixture(scope="session")
def session_login():
    chromedriver = PATH("../../software/chromedriver.exe")
    os.environ['webdriver.chrome.driver'] = chromedriver
    global driver
    driver = webdriver.Chrome(chromedriver)
    driver.get(LD.get_url['url'])
    driver.maximize_window()
    driver.implicitly_wait(20)
    loc(driver).get_login_click()
    auth = Auth(driver).auth_all('../img/img_03.png')
    loc(driver).get_login(LD.login_data["username"], LD.login_data["password"], auth)
    loc(driver).get_system()

    yield driver
    driver.quit()