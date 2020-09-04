import pytest

driver = None


@pytest.fixture(scope='class')
def start_module(project_session_start):
    global driver
    driver = project_session_start
    driver.get('http://192.168.0.156:8901/')
    yield driver
    driver.quit()
