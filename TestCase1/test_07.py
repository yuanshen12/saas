import pytest, allure
from Locators.DealerLocators.purchase.subscribe import Subscribe as loc
from TestCase1 import dealer_datas as LD


class TestSystem():

    @pytest.mark.smoke
    @allure.story("申购")
    def test_35(self, dealer_session_login):
        self.driver = dealer_session_login
        subscribe = loc(self.driver).get_a()
        assert subscribe is True

    @pytest.mark.smoke
    @allure.story("申购")
    @pytest.mark.parametrize("data", LD.sg)
    def test_36(self, dealer_session_login, data):
        self.driver = dealer_session_login
        subscribe = loc(self.driver).get_b(data['add_name'], data['add_num'])
        assert subscribe is True

    @pytest.mark.smoke
    @allure.story("申购")
    @pytest.mark.parametrize("data", LD.sg)
    def test_37(self, dealer_session_login, data):
        self.driver = dealer_session_login
        subscribe = loc(self.driver).get_c(data['add_name'], data['add_num'])
        assert subscribe is True

    @pytest.mark.smoke
    @allure.story("申购")
    def test_38(self, dealer_session_login):
        self.driver = dealer_session_login
        subscribe = loc(self.driver).get_d()
        assert subscribe is True

    @pytest.mark.smoke
    @allure.story("申购")
    def test_39(self, dealer_session_login):
        self.driver = dealer_session_login
        subscribe = loc(self.driver).get_cd()
        assert subscribe is True

    @pytest.mark.smoke
    @allure.story("申购")
    def test_40(self, dealer_session_login):
        self.driver = dealer_session_login
        subscribe = loc(self.driver).get_e()
        assert subscribe is True

    @pytest.mark.smoke
    @allure.story("申购")
    def test_41(self, dealer_session_login):
        self.driver = dealer_session_login
        subscribe = loc(self.driver).get_f()
        assert subscribe is True

    @pytest.mark.smoke
    @allure.story("申购")
    def test_43(self, dealer_session_login):
        self.driver = dealer_session_login
        subscribe = loc(self.driver).get_h()
        assert subscribe is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_07.py'])