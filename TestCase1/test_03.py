import pytest, allure
from Locators.DealerLocators.system.role import Role as loc
from TestCase1 import dealer_datas as LD


class TestSystem():

    @pytest.mark.smoke
    @allure.story("角色管理")
    @pytest.mark.parametrize("data", LD.rl)
    def test_10(self, dealer_session_login, data):
        self.driver = dealer_session_login
        role = loc(self.driver).get_a(data['add_1'])
        assert role is True

    @pytest.mark.smoke
    @allure.story("角色管理")
    def test_11(self, dealer_session_login):
        self.driver = dealer_session_login
        role = loc(self.driver).get_b()
        assert role is True

    @pytest.mark.smoke
    @allure.story("角色管理")
    @pytest.mark.parametrize("data", LD.rl)
    def test_12(self, dealer_session_login, data):
        self.driver = dealer_session_login
        role = loc(self.driver).get_a(data['add_2'])
        assert role is True

    @pytest.mark.smoke
    @allure.story("角色管理")
    def test_13(self, dealer_session_login):
        self.driver = dealer_session_login
        role = loc(self.driver).get_b(num=1)
        assert role is True

    @pytest.mark.smoke
    @allure.story("角色管理")
    @pytest.mark.parametrize("data", LD.rl)
    def test_14(self, dealer_session_login, data):
        self.driver = dealer_session_login
        role = loc(self.driver).get_a(data['add_3'])
        assert role is True

    @pytest.mark.smoke
    @allure.story("角色管理")
    def test_15(self, dealer_session_login):
        self.driver = dealer_session_login
        role = loc(self.driver).get_b(num=2)
        assert role is True

    @pytest.mark.smoke
    @allure.story("角色管理")
    @pytest.mark.parametrize("data", LD.rl)
    def test_16(self, dealer_session_login, data):
        self.driver = dealer_session_login
        role = loc(self.driver).get_c(data['add'])
        assert role is True

    @pytest.mark.smoke
    @allure.story("角色管理")
    def test_17(self, dealer_session_login):
        self.driver = dealer_session_login
        role = loc(self.driver).get_d()
        assert role is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_03.py'])