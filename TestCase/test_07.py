import pytest, allure
from Locators.LabLocators.system.warehouse import Warehouse as loc_wh
from TestCase import lab_datas as LD


class TestSystem():

    @pytest.mark.smoke
    @allure.story("仓库信息")
    @pytest.mark.parametrize("data", LD.add_warehouse_name)
    def test_37(self, session_login, data):
        self.driver = session_login
        warehouse = loc_wh(self.driver).add_warehouse(data["add_name"])
        assert warehouse is True

    @pytest.mark.smoke
    @allure.story("仓库信息")
    @pytest.mark.parametrize("data", LD.add_warehouse_name)
    def test_38(self, session_login, data):
        self.driver = session_login
        warehouse = loc_wh(self.driver).search_wh(data["add_name"])
        assert warehouse == data["add_name"]

    @pytest.mark.smoke
    @allure.story("仓库信息")
    @pytest.mark.parametrize("data", LD.alter_warehouse_name)
    def test_39(self, session_login, data):
        self.driver = session_login
        warehouse = loc_wh(self.driver).alter_wh(data["alter_name"])
        assert warehouse == data["alter_name"]

    @pytest.mark.smoke
    @allure.story("仓库信息")
    def test_40(self, session_login):
        self.driver = session_login
        warehouse = loc_wh(self.driver).del_wh()
        assert warehouse is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_07.py'])