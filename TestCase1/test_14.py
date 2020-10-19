import pytest, allure
from Locators.DealerLocators.inventory.warehouse import Warehouse as loc
from TestCase1 import dealer_datas as LD


class TestSystem():

    @pytest.mark.smoke
    @allure.story("仓库")
    def test_74(self, dealer_session_login):
        self.driver = dealer_session_login
        warehouse = loc(self.driver).get_a()
        assert warehouse is True

    @pytest.mark.smoke
    @allure.story("仓库")
    @pytest.mark.parametrize("data", LD.pd)
    def test_75(self, dealer_session_login, data):
        self.driver = dealer_session_login
        warehouse = loc(self.driver).get_b(data['add_name'])
        assert warehouse is True

    @pytest.mark.smoke
    @allure.story("仓库")
    def test_76(self, dealer_session_login):
        self.driver = dealer_session_login
        warehouse = loc(self.driver).get_c()
        assert warehouse is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_14.py'])