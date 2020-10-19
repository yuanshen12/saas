import pytest, allure
from Locators.DealerLocators.inventory.inventory import Inventory as loc
from TestCase1 import dealer_datas as LD


class TestSystem():

    @pytest.mark.smoke
    @allure.story("库存")
    def test_61(self, dealer_session_login):
        self.driver = dealer_session_login
        inventory = loc(self.driver).get_a()
        assert inventory is True

    @pytest.mark.smoke
    @allure.story("库存")
    @pytest.mark.parametrize("data", LD.rk)
    def test_62(self, dealer_session_login, data):
        self.driver = dealer_session_login
        inventory = loc(self.driver).get_b(data["add_name"], data["add_num"])
        assert inventory is True

    @pytest.mark.smoke
    @allure.story("库存")
    def test_63(self, dealer_session_login):
        self.driver = dealer_session_login
        inventory = loc(self.driver).get_c()
        assert inventory is True

    @pytest.mark.smoke
    @allure.story("库存")
    @pytest.mark.parametrize("data", LD.rk)
    def test_64(self, dealer_session_login, data):
        self.driver = dealer_session_login
        inventory = loc(self.driver).get_d(data["add_num"])
        assert inventory is True

    @pytest.mark.smoke
    @allure.story("库存")
    @pytest.mark.parametrize("data", LD.rk)
    def test_65(self, dealer_session_login, data):
        self.driver = dealer_session_login
        inventory = loc(self.driver).get_e(data["add_name"])
        assert inventory is True

    @pytest.mark.smoke
    @allure.story("库存")
    def test_66(self, dealer_session_login):
        self.driver = dealer_session_login
        inventory = loc(self.driver).get_f()
        assert inventory is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_12.py'])