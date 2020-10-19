import pytest, allure
from Locators.DealerLocators.system.commodity import Commodity as loc
from TestCase1 import dealer_datas as LD


class TestSystem():

    @pytest.mark.smoke
    @allure.story("商品基础信息")
    def test_18(self, dealer_session_login):
        self.driver = dealer_session_login
        commodity = loc(self.driver).get_a()
        assert commodity is True

    @pytest.mark.smoke
    @allure.story("商品基础信息")
    @pytest.mark.parametrize("data", LD.sp)
    def test_19(self, dealer_session_login, data):
        self.driver = dealer_session_login
        commodity = loc(self.driver).get_b(data["add_name"])
        assert commodity is True

    @pytest.mark.smoke
    @allure.story("商品基础信息")
    @pytest.mark.parametrize("data", LD.sp)
    def test_20(self, dealer_session_login, data):
        self.driver = dealer_session_login
        commodity = loc(self.driver).get_c(data["add_num"])
        assert commodity is True

    @pytest.mark.smoke
    @allure.story("商品基础信息")
    @pytest.mark.parametrize("data", LD.sp)
    def test_21(self, dealer_session_login, data):
        self.driver = dealer_session_login
        commodity = loc(self.driver).get_d(data["add_nums"])
        assert commodity is True

    @pytest.mark.smoke
    @allure.story("商品基础信息")
    @pytest.mark.parametrize("data", LD.sp)
    def test_22(self, dealer_session_login, data):
        self.driver = dealer_session_login
        commodity = loc(self.driver).get_f(data["add_nums"], data['add_num'])
        assert commodity is True

    @pytest.mark.smoke
    @allure.story("商品基础信息")
    @pytest.mark.parametrize("data", LD.sp)
    def test_23(self, dealer_session_login, data):
        self.driver = dealer_session_login
        commodity = loc(self.driver).get_g(data['add_nums'])
        assert commodity is True

    @pytest.mark.smoke
    @allure.story("商品基础信息")
    @pytest.mark.parametrize("data", LD.sp)
    def test_24(self, dealer_session_login, data):
        self.driver = dealer_session_login
        commodity = loc(self.driver).get_h(data['add_1'])
        assert commodity is True

    @pytest.mark.smoke
    @allure.story("商品基础信息")
    def test_25(self, dealer_session_login):
        self.driver = dealer_session_login
        commodity = loc(self.driver).get_j()
        assert commodity is True

    @pytest.mark.smoke
    @allure.story("商品基础信息")
    @pytest.mark.parametrize("data", LD.sp)
    def test_26(self, dealer_session_login, data):
        self.driver = dealer_session_login
        commodity = loc(self.driver).get_k(data['add_bq'])
        assert commodity is True

    @pytest.mark.smoke
    @allure.story("商品基础信息")
    def test_27(self, dealer_session_login):
        self.driver = dealer_session_login
        commodity = loc(self.driver).get_s()
        assert commodity is True

    @pytest.mark.smoke
    @allure.story("商品基础信息")
    @pytest.mark.skip("the is bug!")
    @pytest.mark.parametrize("data", LD.sp)
    def test_28(self, dealer_session_login, data):
        self.driver = dealer_session_login
        commodity = loc(self.driver).get_z(data['add_name'])
        assert commodity is True

    @pytest.mark.smoke
    @allure.story("商品基础信息")
    def test_29(self, dealer_session_login):
        self.driver = dealer_session_login
        commodity = loc(self.driver).get_w()
        assert commodity is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_04.py'])