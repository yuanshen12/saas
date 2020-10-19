import pytest, allure
from Locators.LabLocators.system.role import Role as loc_role
from TestCase import lab_datas as LD


class TestSystem():

    @allure.story("角色管理")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_role_name)
    def test_16(self, session_login, data):
        self.driver = session_login
        loc_add = loc_role(self.driver).add_role(data["add_1"])
        assert loc_add == data["add_1"]

    @allure.story("角色管理")
    @pytest.mark.smoke
    def test_17(self, session_login):
        self.driver = session_login
        loc_alter = loc_role(self.driver).alter_role()
        assert len(loc_alter) > 10

    @allure.story("角色管理")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_role_name)
    def test_18(self, session_login, data):
        self.driver = session_login
        at = loc_role(self.driver).add_t(data["add_2"])
        assert at is True

    @allure.story("角色管理")
    @pytest.mark.smoke
    def test_19(self, session_login):
        self.driver = session_login
        ta = loc_role(self.driver).alter_t()
        assert ta is True

    @allure.story("角色管理")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_role_name)
    def test_20(self, session_login, data):
        self.driver = session_login
        ss = loc_role(self.driver).get_ss(data["add"])
        assert ss is True

    @allure.story("角色管理")
    @pytest.mark.smoke
    def test_21(self, session_login):
        self.driver = session_login
        loc_del = loc_role(self.driver).del_role()
        assert loc_del is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_03.py'])