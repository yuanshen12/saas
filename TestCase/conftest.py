from selenium import webdriver
import pytest
import os
driver = None
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


@pytest.fixture(scope='session')
def project_session_start():

    chromedriver = PATH("../software/chromedriver.exe")
    os.environ['webdriver.chrome.driver'] = chromedriver
    global driver
    driver = webdriver.Chrome(chromedriver)
    driver.maximize_window()

    yield driver
    driver.quit()

