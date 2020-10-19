import pytest, allure
from Locators.DealerLocators.purchase.supplier import Supplier as loc
from TestCase1 import dealer_datas as LD


class TestSystem():

    @pytest.mark.smoke
    @allure.story("供应商信息")
    def test_54(self, dealer_session_login):
        self.driver = dealer_session_login
        supplier = loc(self.driver).get_a()
        assert supplier is True

    @pytest.mark.smoke
    @allure.story("供应商信息")
    @pytest.mark.parametrize("data", LD.gy)
    def test_55(self, dealer_session_login, data):
        self.driver = dealer_session_login
        supplier = loc(self.driver).get_b(data['add_name'])
        assert supplier is True

    @pytest.mark.smoke
    @allure.story("供应商信息")
    @pytest.mark.parametrize("data", LD.gy)
    def test_56(self, dealer_session_login, data):
        self.driver = dealer_session_login
        supplier = loc(self.driver).get_c(data['add_name'])
        assert supplier is True

    @pytest.mark.smoke
    @allure.story("供应商信息")
    def test_57(self, dealer_session_login):
        self.driver = dealer_session_login
        supplier = loc(self.driver).get_d()
        assert supplier is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_09.py'])