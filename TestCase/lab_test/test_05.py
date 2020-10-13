import pytest, allure
from Locators.LabLocators.system.supplier import Supplier as loc_supplier
from TestCase.lab_test import lab_datas as LD


class TestSystem():

    @allure.story("供应商信息")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_supplier_name)
    def test_19(self, session_login, data):
        self.driver = session_login
        supplier_text = loc_supplier(self.driver).add_supplier(data["add_name"])
        assert supplier_text == data["add_name"]

    @allure.story("供应商信息")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_supplier_name)
    def test_20(self, session_login, data):
        self.driver = session_login
        search = loc_supplier(self.driver).search_supplier(data["add_name"])
        assert search == data["add_name"]

    @allure.story("供应商信息")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.alter_name)
    def test_21(self, session_login, data):
        self.driver = session_login
        search = loc_supplier(self.driver).alter_supplier(data["alter_name"])
        assert search == data["alter_name"]

    @allure.story("供应商信息")
    @pytest.mark.smoke
    def test_22(self, session_login):
        self.driver = session_login
        del_su = loc_supplier(self.driver).del_supplier()
        assert del_su is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_05.py'])