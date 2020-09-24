import pytest, allure
from Locators.LabLocators.subscribe import Subscribe as loc
from Locators.LabLocators.role import Role as loc_role
from TestCase.lab_test import lab_datas as LD


class TestSystem():

    @allure.story("开启账户资金")
    @pytest.mark.smoke
    def test_01(self, session_login):
        self.driver = session_login
        subscribe = loc(self.driver).get_subscribe("fend_start")
        assert subscribe is True

    @allure.story("新增项目组")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_name)
    def test_02(self, session_login, data):
        self.driver = session_login
        loc_add = loc(self.driver).get_add_sub(data["add_name"])
        assert loc_add == data["add_name"]

    @allure.story("修改项目组")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.alter_name)
    def test_03(self, session_login, data):
        self.driver = session_login
        loc_alter = loc(self.driver).get_details(data["alter_name"])
        assert loc_alter == data["alter_name"]

    @allure.story("删除项目组")
    @pytest.mark.smoke
    def test_04(self, session_login):
        self.driver = session_login
        loc_del = loc(self.driver).get_del()
        assert loc_del is True

    @allure.story("新增角色")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_role_name)
    def test_05(self, session_login, data):
        self.driver = session_login
        loc_add = loc_role(self.driver).add_role(data["add_name"])
        assert loc_add == data["add_name"]

    @allure.story("修改角色权限")
    @pytest.mark.smoke
    def test_06(self, session_login):
        self.driver = session_login
        loc_alter = loc_role(self.driver).alter_role()
        assert len(loc_alter) > 10

    @allure.story("删除角色")
    @pytest.mark.smoke
    def test_07(self, session_login):
        self.driver = session_login
        loc_del = loc_role(self.driver).del_role()
        assert loc_del is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_system.py'])