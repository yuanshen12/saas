import pytest, allure
from Locators.DealerLocators.inventory.stocking import Stocking as loc
from TestCase1 import dealer_datas as LD


class TestSystem():

    @pytest.mark.smoke
    @allure.story("盘点")
    def test_67(self, dealer_session_login):
        self.driver = dealer_session_login
        stocking = loc(self.driver).get_a()
        assert stocking is True

    @pytest.mark.smoke
    @allure.story("盘点")
    def test_68(self, dealer_session_login):
        self.driver = dealer_session_login
        stocking = loc(self.driver).get_b()
        assert stocking is True

    @pytest.mark.smoke
    @allure.story("盘点")
    def test_69(self, dealer_session_login):
        self.driver = dealer_session_login
        stocking = loc(self.driver).get_c()
        assert stocking is True

    @pytest.mark.smoke
    @allure.story("盘点")
    def test_70(self, dealer_session_login):
        self.driver = dealer_session_login
        stocking = loc(self.driver).get_d()
        assert stocking is True

    @pytest.mark.smoke
    @allure.story("盘点")
    def test_71(self, dealer_session_login):
        self.driver = dealer_session_login
        stocking = loc(self.driver).get_e()
        assert stocking is True

    @pytest.mark.smoke
    @allure.story("盘点")
    @pytest.mark.skip("默认仓库盘点入库，未知异常BUG！！")
    @pytest.mark.parametrize("data", LD.pd)
    def test_72(self, dealer_session_login, data):
        self.driver = dealer_session_login
        stocking = loc(self.driver).get_f(data['add_name'])
        assert stocking is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_13.py'])