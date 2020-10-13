import pytest, allure
from Locators.LabLocators.system.subscribe import Subscribe as loc
from TestCase.lab_test import lab_datas as LD


class TestSystem():

    @allure.story("实验室管理")
    @pytest.mark.smoke
    def test_07(self, session_login):
        self.driver = session_login
        subscribe = loc(self.driver).get_subscribe("fend_start")
        assert subscribe is True

    @allure.story("实验室管理")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_name)
    def test_08(self, session_login, data):
        self.driver = session_login
        gr = loc(self.driver).get_gr(data["add_num"])
        assert gr is True

    @allure.story("实验室管理")
    @pytest.mark.smoke
    def test_09(self, session_login):
        self.driver = session_login
        sq = loc(self.driver).get_sq()
        assert sq is True

    @allure.story("实验室管理")
    @pytest.mark.smoke
    def test_10(self, session_login):
        self.driver = session_login
        yw = loc(self.driver).get_y(2)
        assert yw is True

    @allure.story("实验室管理")
    @pytest.mark.smoke
    def test_11(self, session_login):
        self.driver = session_login
        yw = loc(self.driver).get_y(1)
        assert yw is True

    @allure.story("实验室管理")
    @pytest.mark.smoke
    def test_12(self, session_login):
        self.driver = session_login
        yw = loc(self.driver).get_y(0)
        assert yw is True

    @allure.story("实验室管理")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_name)
    def test_13(self, session_login, data):
        self.driver = session_login
        loc_add = loc(self.driver).get_add_sub(data["add_name"])
        assert loc_add == data["add_name"]

    @allure.story("实验室管理")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.alter_name)
    def test_14(self, session_login, data):
        self.driver = session_login
        loc_alter = loc(self.driver).get_details(data["alter_name"])
        assert loc_alter == data["alter_name"]

    @allure.story("实验室管理")
    @pytest.mark.smoke
    def test_15(self, session_login):
        self.driver = session_login
        loc_del = loc(self.driver).get_del()
        assert loc_del is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_02.py'])