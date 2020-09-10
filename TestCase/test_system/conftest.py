import pytest
from Locators.SystemLocators.system_locators import SystemLocators as loc
driver = None


@pytest.fixture(scope="class")
def start_module(project_session_login):
    global driver
    driver = project_session_login
    driver.implicitly_wait(20)
    loc(driver).get_system()

    yield driver
    driver.quit()
