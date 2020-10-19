import pytest, allure
from Locators.DealerLocators.system.tissue import Tissue as loc
from TestCase1 import dealer_datas as LD


class TestSystem():

    @pytest.mark.smoke
    @allure.story("组织架构")
    def test_06(self, dealer_session_login):
        self.driver = dealer_session_login
        tissue = loc(self.driver).get_a()
        assert tissue is True

    @pytest.mark.smoke
    @allure.story("组织架构")
    def test_07(self, dealer_session_login):
        self.driver = dealer_session_login
        tissue = loc(self.driver).get_b()
        assert tissue is True

    @pytest.mark.smoke
    @allure.story("组织架构")
    @pytest.mark.parametrize("data", LD.ts)
    def test_08(self, dealer_session_login, data):
        self.driver = dealer_session_login
        tissue = loc(self.driver).get_c(data["add_name"])
        assert tissue is True

    @pytest.mark.smoke
    @allure.story("组织架构")
    @pytest.mark.parametrize("data", LD.ts)
    def test_09(self, dealer_session_login, data):
        self.driver = dealer_session_login
        tissue = loc(self.driver).get_d(data["add_b"])
        assert tissue is True

    @pytest.mark.smoke
    @allure.story("组织架构")
    def test_10(self, dealer_session_login):
        self.driver = dealer_session_login
        tissue = loc(self.driver).get_f()
        assert tissue is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_02.py'])