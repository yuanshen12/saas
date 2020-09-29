import pytest, allure
from Locators.LabLocators.system.subscribe import Subscribe as loc
from Locators.LabLocators.system.role import Role as loc_role
from Locators.LabLocators.system.reagent import Reagent as loc_reagent
from Locators.LabLocators.system.supplier import Supplier as loc_supplier
from Locators.LabLocators.system.home import Home as loc_home
from Locators.LabLocators.system.warehouse import Warehouse as loc_wh
from Locators.LabLocators.system.check import Check as loc_check
from TestCase.lab_test import lab_datas as LD


class TestSystem():

    @allure.story("实验室管理")
    @pytest.mark.smoke
    def test_01(self, session_login):
        self.driver = session_login
        subscribe = loc(self.driver).get_subscribe("fend_start")
        assert subscribe is True

    @allure.story("实验室管理")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_name)
    def test_02(self, session_login, data):
        self.driver = session_login
        loc_add = loc(self.driver).get_add_sub(data["add_name"])
        assert loc_add == data["add_name"]

    @allure.story("实验室管理")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.alter_name)
    def test_03(self, session_login, data):
        self.driver = session_login
        loc_alter = loc(self.driver).get_details(data["alter_name"])
        assert loc_alter == data["alter_name"]

    @allure.story("实验室管理")
    @pytest.mark.smoke
    def test_04(self, session_login):
        self.driver = session_login
        loc_del = loc(self.driver).get_del()
        assert loc_del is True

    @allure.story("角色管理")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_role_name)
    def test_05(self, session_login, data):
        self.driver = session_login
        loc_add = loc_role(self.driver).add_role(data["add_name"])
        assert loc_add == data["add_name"]

    @allure.story("角色管理")
    @pytest.mark.smoke
    def test_06(self, session_login):
        self.driver = session_login
        loc_alter = loc_role(self.driver).alter_role()
        assert len(loc_alter) > 10

    @allure.story("角色管理")
    @pytest.mark.smoke
    def test_07(self, session_login):
        self.driver = session_login
        loc_del = loc_role(self.driver).del_role()
        assert loc_del is True

    @allure.story("试剂耗材信息")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_reagent_name)
    def test_08(self, session_login, data):
        self.driver = session_login
        reagent = loc_reagent(self.driver).add_reagent(data["add_name"])
        assert reagent is True

    @allure.story("试剂耗材信息")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_reagent_name)
    def test_09(self, session_login, data):
        self.driver = session_login
        search = loc_reagent(self.driver).search_name(data["add_name"])
        assert search == data["add_name"]

    @allure.story("试剂耗材信息")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_reagent_cas)
    def test_10(self, session_login, data):
        self.driver = session_login
        add_go = loc_reagent(self.driver).alter_reagent(data["add_cas"])
        assert add_go is True

    @allure.story("试剂耗材信息")
    @pytest.mark.smoke
    @pytest.mark.skip(reason="这是一个BUG！！")
    def test_11(self, session_login):
        self.driver = session_login
        del_ensure = loc_reagent(self.driver).del_reagent()
        assert del_ensure is True

    @allure.story("供应商信息")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_supplier_name)
    def test_12(self, session_login, data):
        self.driver = session_login
        supplier_text = loc_supplier(self.driver).add_supplier(data["add_name"])
        assert supplier_text == data["add_name"]

    @allure.story("供应商信息")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_supplier_name)
    def test_13(self, session_login, data):
        self.driver = session_login
        search = loc_supplier(self.driver).search_supplier(data["add_name"])
        assert search == data["add_name"]

    @allure.story("供应商信息")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.alter_name)
    def test_14(self, session_login, data):
        self.driver = session_login
        search = loc_supplier(self.driver).alter_supplier(data["alter_name"])
        assert search == data["alter_name"]

    @allure.story("供应商信息")
    @pytest.mark.smoke
    def test_15(self, session_login):
        self.driver = session_login
        del_su = loc_supplier(self.driver).del_supplier()
        assert del_su is True

    @pytest.mark.smoke
    @pytest.mark.skip("这是个问题！！")
    @pytest.mark.parametrize("data", LD.add_home_name)
    def test_16(self, session_login, data):
        self.driver = session_login
        add_home = loc_home(self.driver).add_home(data["add_name"])
        assert add_home is True

    @pytest.mark.smoke
    @allure.story("房间信息")
    @pytest.mark.parametrize("data", LD.add_home_name)
    def test_17(self, session_login, data):
        self.driver = session_login
        home_text = loc_home(self.driver).search_home(data["add_name"])
        assert home_text == data["add_name"]

    @pytest.mark.smoke
    @allure.story("房间信息")
    @pytest.mark.parametrize("data", LD.alter_home_name)
    def test_18(self, session_login, data):
        self.driver = session_login
        home_text = loc_home(self.driver).alter_home(data["alter_name"])
        assert home_text == data["alter_name"]

    @pytest.mark.smoke
    @allure.story("仓库信息")
    @pytest.mark.parametrize("data", LD.add_warehouse_name)
    def test_19(self, session_login, data):
        self.driver = session_login
        warehouse = loc_wh(self.driver).add_warehouse(data["add_name"])
        assert warehouse is True

    @pytest.mark.smoke
    @allure.story("仓库信息")
    @pytest.mark.parametrize("data", LD.add_warehouse_name)
    def test_20(self, session_login, data):
        self.driver = session_login
        warehouse = loc_wh(self.driver).search_wh(data["add_name"])
        assert warehouse == data["add_name"]

    @pytest.mark.smoke
    @allure.story("仓库信息")
    @pytest.mark.parametrize("data", LD.alter_warehouse_name)
    def test_21(self, session_login, data):
        self.driver = session_login
        warehouse = loc_wh(self.driver).alter_wh(data["alter_name"])
        assert warehouse == data["alter_name"]

    @pytest.mark.smoke
    @allure.story("仓库信息")
    def test_22(self, session_login):
        self.driver = session_login
        warehouse = loc_wh(self.driver).del_wh()
        assert warehouse is True

    @pytest.mark.smoke
    @allure.story("审核流程")
    def test_23(self, session_login):
        self.driver = session_login
        check = loc_check(self.driver).alter_check_yes()
        assert check is True

    @pytest.mark.smoke
    @allure.story("审核流程")
    def test_24(self, session_login):
        self.driver = session_login
        check = loc_check(self.driver).alter_check_no()
        assert check is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_01.py'])