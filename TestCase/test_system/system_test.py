import pytest, allure
from Locators.SystemLocators.subscribe_locators import SubscribeLocators as loc
from Locators.SystemLocators.role_locators import RoleLocators as loc_role
from TestDatas.SystemDatas import system_datas as LD


class TestSystem():

    @allure.story("实验室管理开启账户资金")
    @pytest.mark.smoke
    def test_01(self, start_module):
        self.driver = start_module
        loc_subscribe = loc(self.driver).get_subscribe("fend_start")
        assert loc_subscribe is True

    @allure.story("实验室管理新增项目组")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_name)
    def test_02(self, start_module, data):
        self.driver = start_module
        loc_add = loc(self.driver).get_add_sub(data["add_name"])
        assert loc_add == data["add_name"]

    @allure.story("实验室管理修改项目组")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.alter_name)
    def test_03(self, start_module, data):
        self.driver = start_module
        loc_alter = loc(self.driver).get_details(data["alter_name"])
        assert loc_alter == data["alter_name"]

    @allure.story("实验室管理删除项目组")
    @pytest.mark.smoke
    def test_04(self, start_module):
        self.driver = start_module
        loc_del = loc(self.driver).get_del()
        assert loc_del is True

    @allure.story("角色管理新增角色")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_role_name)
    def test_05(self, start_module, data):
        self.driver = start_module
        loc_add = loc_role(self.driver).add_role(data["add_name"])
        assert loc_add == data["add_name"]

    @allure.story("角色管理修改角色权限")
    @pytest.mark.smoke
    def test_06(self, start_module):
        self.driver = start_module
        loc_alter = loc_role(self.driver).alter_role()
        assert len(loc_alter) > 10

    @allure.story("角色管理删除角色")
    @pytest.mark.smoke
    def test_07(self, start_module):
        self.driver = start_module
        loc_del = loc_role(self.driver).del_role()
        assert loc_del is True


if __name__ == '__main__':
    pytest.main(["-s", "system_test.py"])

