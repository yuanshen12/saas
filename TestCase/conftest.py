from selenium import webdriver
import pytest
import os
from TestDatas.GobalDatas import gobal_datas as GD
from Locators.LoginLocators.login_locators import LoginLocators as loc
from TestDatas.LoginDatas.login_datas import success_login as LD
from common.common_auth import Auth


driver = None
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


@pytest.fixture(scope='session')
def project_session_start():

    chromedriver = PATH("../software/chromedriver.exe")
    os.environ['webdriver.chrome.driver'] = chromedriver
    global driver
    driver = webdriver.Chrome(chromedriver)
    driver.get(GD.saas_lab_url)
    driver.maximize_window()
    driver.implicitly_wait(20)

    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def project_session_login():
    chromedriver = PATH("../software/chromedriver.exe")
    os.environ['webdriver.chrome.driver'] = chromedriver
    global driver
    driver = webdriver.Chrome(chromedriver)
    driver.get(GD.saas_lab_url)
    driver.maximize_window()
    driver.implicitly_wait(20)
    loc(driver).get_login_click()
    auth = Auth(driver).auth_all('../img/img_03.png')
    loc(driver).get_login(LD["username"], LD["password"], auth)

    yield driver
    driver.quit()

