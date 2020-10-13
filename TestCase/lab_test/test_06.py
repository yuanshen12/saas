import pytest, allure
from Locators.LabLocators.system.home import Home as loc_home
from TestCase.lab_test import lab_datas as LD


class TestSystem():

    @pytest.mark.smoke
    @pytest.mark.skip("这是个问题！！")
    @pytest.mark.parametrize("data", LD.add_home_name)
    def test_23(self, session_login, data):
        self.driver = session_login
        add_home = loc_home(self.driver).add_home(data["add_name"])
        assert add_home is True

    @pytest.mark.smoke
    @allure.story("房间信息")
    @pytest.mark.parametrize("data", LD.add_home_name)
    def test_24(self, session_login, data):
        self.driver = session_login
        home_text = loc_home(self.driver).search_home(data["add_name"])
        assert home_text == data["add_name"]

    @pytest.mark.smoke
    @allure.story("房间信息")
    @pytest.mark.parametrize("data", LD.alter_home_name)
    def test_25(self, session_login, data):
        self.driver = session_login
        home_text = loc_home(self.driver).alter_home(data["alter_name"])
        assert home_text == data["alter_name"]


if __name__ == '__main__':
    pytest.main(['-s', 'test_06.py'])