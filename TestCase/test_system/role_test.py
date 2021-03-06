import pytest, allure
from Locators.SystemLocators.reagent_locators import ReagentLocators as loc
from TestDatas.SystemDatas import system_datas as LD


class TestSystem():

    @pytest.mark.parametrize("data", LD.add_reagent_name)
    def test_06(self, start_module, data):
        self.driver = start_module
        reagent = loc(self.driver).add_reagent(data["add_name"])
        assert reagent is True

    @pytest.mark.parametrize("data", LD.add_reagent_name)
    def test_08(self, start_module, data):
        self.driver = start_module
        loc(self.driver).search_name(data["add_name"])
        assert 1 == 0


if __name__ == '__main__':
    pytest.main(['-s', 'role_test.py'])