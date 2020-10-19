import pytest, allure
from Locators.DealerLocators.purchase.purchase import Purchase as loc
from TestCase1 import dealer_datas as LD


class TestSystem():

    @pytest.mark.smoke
    @allure.story("采购")
    def test_44(self, dealer_session_login):
        self.driver = dealer_session_login
        purchase = loc(self.driver).get_a()
        assert purchase is True

    @pytest.mark.smoke
    @allure.story("采购")
    @pytest.mark.parametrize("data", LD.cg)
    def test_45(self, dealer_session_login, data):
        self.driver = dealer_session_login
        purchase = loc(self.driver).get_b(data['add_name'], data['add_names'], data['add_num'])
        assert purchase is True

    @pytest.mark.smoke
    @allure.story("采购")
    @pytest.mark.parametrize("data", LD.cg)
    def test_46(self, dealer_session_login, data):
        self.driver = dealer_session_login
        purchase = loc(self.driver).get_c(data['add_name'])
        assert purchase is True

    @pytest.mark.smoke
    @allure.story("采购")
    @pytest.mark.parametrize("data", LD.cg)
    def test_47(self, dealer_session_login, data):
        self.driver = dealer_session_login
        purchase = loc(self.driver).get_b(data['add_name'], data['add_names'], data['add_num'], choose=1)
        assert purchase is True

    @pytest.mark.smoke
    @allure.story("采购")
    def test_48(self, dealer_session_login):
        self.driver = dealer_session_login
        purchase = loc(self.driver).get_d()
        assert purchase is True

    @pytest.mark.smoke
    @allure.story("采购")
    def test_49(self, dealer_session_login):
        self.driver = dealer_session_login
        purchase = loc(self.driver).get_f()
        assert purchase is True

    @pytest.mark.smoke
    @allure.story("采购")
    def test_50(self, dealer_session_login):
        self.driver = dealer_session_login
        purchase = loc(self.driver).get_g()
        assert purchase is True

    @pytest.mark.smoke
    @allure.story("采购")
    def test_51(self, dealer_session_login):
        self.driver = dealer_session_login
        purchase = loc(self.driver).get_h()
        assert purchase is True

    @pytest.mark.smoke
    @allure.story("采购")
    @pytest.mark.parametrize("data", LD.xj)
    def test_52(self, dealer_session_login, data):
        self.driver = dealer_session_login
        purchase = loc(self.driver).get_j(data['add_mc'], data['add_sl'])
        assert purchase is True

    @pytest.mark.smoke
    @allure.story("采购")
    @pytest.mark.parametrize("data", LD.xj)
    def test_53(self, dealer_session_login, data):
        self.driver = dealer_session_login
        purchase = loc(self.driver).get_k(data['add_name'])
        assert purchase is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_08.py'])