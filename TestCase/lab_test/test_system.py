import pytest, allure
from Locators.LabLocators.subscribe import Subscribe as loc
from Locators.LabLocators.role import Role as loc_role
from Locators.LabLocators.reagent import Reagent as loc_reagent
from Locators.LabLocators.supplier import Supplier as loc_supplier
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

    @allure.story("新增耗材")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_reagent_name)
    def test_08(self, session_login, data):
        self.driver = session_login
        reagent = loc_reagent(self.driver).add_reagent(data["add_name"])
        assert reagent is True

    @allure.story("搜索耗材")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_reagent_name)
    def test_09(self, session_login, data):
        self.driver = session_login
        search = loc_reagent(self.driver).search_name(data["add_name"])
        assert search == data["add_name"]

    @allure.story("修改耗材")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_reagent_cas)
    def test_10(self, session_login, data):
        self.driver = session_login
        add_go = loc_reagent(self.driver).alter_reagent(data["add_cas"])
        assert add_go is True

    @allure.story("删除耗材")
    @pytest.mark.smoke
    @pytest.mark.skip(reason="这是一个BUG！！")
    def test_11(self, session_login):
        self.driver = session_login
        del_ensure = loc_reagent(self.driver).del_reagent()
        assert del_ensure is True

    @allure.story("新增供应商")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_supplier_name)
    def test_12(self, session_login, data):
        self.driver = session_login
        supplier_text = loc_supplier(self.driver).add_supplier(data["add_name"])
        assert supplier_text == data["add_name"]

    @allure.story("搜索供应商")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_supplier_name)
    def test_13(self, session_login, data):
        self.driver = session_login
        search = loc_supplier(self.driver).search_supplier(data["add_name"])
        assert search == data["add_name"]

    @allure.story("修改供应商")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.alter_name)
    def test_14(self, session_login, data):
        self.driver = session_login
        search = loc_supplier(self.driver).alter_supplier(data["alter_name"])
        assert search == data["alter_name"]

    @allure.story("删除供应商")
    @pytest.mark.smoke
    def test_15(self, session_login):
        self.driver = session_login
        del_su = loc_supplier(self.driver).del_supplier()
        assert del_su is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_system.py'])