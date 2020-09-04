from selenium import webdriver
import pytest

driver = None


@pytest.fixture(scope='session')
def project_session_start():

    global driver
    driver = webdriver.Chrome('../software/chromedriver.exe')
    driver.maximize_window()

    yield driver

    driver.quit()

