import pytest, allure
from Locators.DealerLocators.inventory.check import Check as loc
from Locators.DealerLocators.purchase.sales import Sales as loc_s
from TestCase1 import dealer_datas as LD


class TestSystem():

    @pytest.mark.smoke
    @allure.story("验收入库")
    def test_58(self, dealer_session_login):
        self.driver = dealer_session_login
        check = loc(self.driver).get_a()
        assert check is True

    @pytest.mark.smoke
    @allure.story("验收入库")
    @pytest.mark.parametrize("data", LD.ys)
    def test_59(self, dealer_session_login, data):
        self.driver = dealer_session_login
        check = loc(self.driver).get_b(data["add_num"])
        assert check is True

    @pytest.mark.smoke
    @allure.story("采购退货")
    def test_60(self, dealer_session_login):
        self.driver = dealer_session_login
        check = loc_s(self.driver).get_a()
        assert check is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_11.py'])