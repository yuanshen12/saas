import pytest, allure
from Locators.LabLocators.system.member import Member as loc_mb
from TestCase import lab_datas as LD


class TestSystem():

    @allure.story("成员管理")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_c)
    def test_01(self, session_login, data):
        self.driver = session_login
        br = loc_mb(self.driver).add_m(data['add_user'], data['add_name'])
        assert br is True

    @allure.story("成员管理")
    @pytest.mark.smoke
    def test_02(self, session_login):
        self.driver = session_login
        br = loc_mb(self.driver).get_t()
        assert br is True

    @allure.story("成员管理")
    @pytest.mark.smoke
    def test_03(self, session_login):
        self.driver = session_login
        br = loc_mb(self.driver).get_q()
        assert br is True

    @allure.story("成员管理")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_c)
    def test_04(self, session_login, data):
        self.driver = session_login
        br = loc_mb(self.driver).get_ss(data['add_name'])
        assert br is True

    @allure.story("成员管理")
    @pytest.mark.smoke
    def test_05(self, session_login):
        self.driver = session_login
        br = loc_mb(self.driver).get_z()
        assert br is True

    @allure.story("成员管理")
    @pytest.mark.smoke
    def test_06(self, session_login):
        self.driver = session_login
        br = loc_mb(self.driver).get_s()
        assert br is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_01.py'])