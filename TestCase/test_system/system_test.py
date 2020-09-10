import pytest
from Locators.SystemLocators.subscribe_locators import SubscribeLocators as loc
from TestDatas.SystemDatas import system_datas as LD


class TestSystem():

    @pytest.mark.smoke
    def test_01(self, start_module):
        self.driver = start_module
        loc_subscribe = loc(self.driver).get_subscribe("fend_start")
        assert loc_subscribe is True

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_name)
    def test_02(self, start_module, data):
        self.driver = start_module
        loc_add = loc(self.driver).get_add_sub(data["add_name"])
        assert loc_add == data["add_name"]

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.alter_name)
    def test_03(self, start_module, data):
        self.driver = start_module
        loc_alter = loc(self.driver).get_details(data["alter_name"])
        assert loc_alter == data["alter_name"]

    @pytest.mark.smoke
    def test_04(self, start_module):
        self.driver = start_module
        loc_del = loc(self.driver).get_del()
        assert loc_del is True


if __name__ == '__main__':
    pytest.main(["-s", "system_test.py"])

