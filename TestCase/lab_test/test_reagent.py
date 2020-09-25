import pytest, allure
from Locators.LabLocators.supplier import Supplier as loc
from TestCase.lab_test import lab_datas as LD


class TestSystem():

    @pytest.mark.parametrize("data", LD.add_supplier_name)
    def test_12(self, session_login, data):
        self.driver = session_login
        supplier_text = loc(self.driver).add_supplier(data["add_name"])
        assert supplier_text == data["add_name"]

    @pytest.mark.parametrize("data", LD.add_supplier_name)
    def test_13(self, session_login, data):
        self.driver = session_login
        search = loc(self.driver).search_supplier(data["add_name"])
        assert search == data["add_name"]

    @pytest.mark.parametrize("data", LD.alter_name)
    def test_14(self, session_login, data):
        self.driver = session_login
        search = loc(self.driver).alter_supplier(data["alter_name"])
        assert search == data["alter_name"]

    def test_15(self, session_login):
        self.driver = session_login
        del_su = loc(self.driver).del_supplier()
        assert del_su is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_reagent.py'])