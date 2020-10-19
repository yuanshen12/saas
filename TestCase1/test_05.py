import pytest, allure
from Locators.DealerLocators.system.examine import Examine as loc


class TestSystem():

    @pytest.mark.smoke
    @allure.story("审核流程")
    def test_30(self, dealer_session_login):
        self.driver = dealer_session_login
        commodity = loc(self.driver).get_a(choose=0)
        assert commodity is True

    @pytest.mark.smoke
    @allure.story("审核流程")
    def test_31(self, dealer_session_login):
        self.driver = dealer_session_login
        commodity = loc(self.driver).get_a(choose=1)
        assert commodity is True

    @pytest.mark.smoke
    @allure.story("审核流程")
    def test_32(self, dealer_session_login):
        self.driver = dealer_session_login
        commodity = loc(self.driver).get_a(choose=2)
        assert commodity is True

    @pytest.mark.smoke
    @allure.story("审核流程")
    def test_33(self, dealer_session_login):
        self.driver = dealer_session_login
        commodity = loc(self.driver).get_a(choose=3)
        assert commodity is True

    @pytest.mark.smoke
    @allure.story("审核流程")
    def test_34(self, dealer_session_login):
        self.driver = dealer_session_login
        commodity = loc(self.driver).get_a(choose=4)
        assert commodity is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_05.py'])