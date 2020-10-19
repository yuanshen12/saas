import pytest, allure
from Locators.DealerLocators.system.member import Member as loc
from TestCase1 import dealer_datas as LD


class TestSystem():

    @pytest.mark.smoke
    @allure.story("成员管理")
    def test_01(self, dealer_session_login):
        self.driver = dealer_session_login
        purchase = loc(self.driver).get_a()
        assert purchase is True

    @pytest.mark.smoke
    @allure.story("成员管理")
    @pytest.mark.parametrize("data", LD.mb)
    def test_02(self, dealer_session_login, data):
        self.driver = dealer_session_login
        purchase = loc(self.driver).get_b(data["add_user"], data["add_name"])
        assert purchase is True

    @pytest.mark.smoke
    @allure.story("成员管理")
    @pytest.mark.parametrize("data", LD.mb)
    def test_03(self, dealer_session_login, data):
        self.driver = dealer_session_login
        purchase = loc(self.driver).get_c(data["add_name"])
        assert purchase is True

    @pytest.mark.smoke
    @allure.story("成员管理")
    def test_04(self, dealer_session_login):
        self.driver = dealer_session_login
        purchase = loc(self.driver).get_d()
        assert purchase is True

    @pytest.mark.smoke
    @allure.story("成员管理")
    @pytest.mark.parametrize("data", LD.mb)
    def test_05(self, dealer_session_login, data):
        self.driver = dealer_session_login
        purchase = loc(self.driver).get_f(data['add_name'])
        assert purchase is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_01.py'])