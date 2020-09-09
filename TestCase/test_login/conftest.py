import pytest
from Locators.LoginLocators.login_locators import LoginLocators as loc
driver = None


@pytest.fixture(scope='class')
def start_module(project_session_start):
    global driver
    driver = project_session_start
    loc(driver).get_login_click()

    yield driver
    driver.quit()


