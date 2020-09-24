import pytest
from Locators.SystemLocators.system_locators import SystemLocators as loc
from TestDatas.SystemDatas import system_datas as LD


class TestSystem():

    @pytest.mark.parametrize("data", LD.add_reagent_name)
    def test_06(self, dealer_session_login, data):
        self.driver = dealer_session_login
        reagent = loc(self.driver).add_reagent(data["add_name"])
        assert reagent is True

    @pytest.mark.parametrize("data", LD.add_reagent_name)
    def test_08(self, dealer_session_login, data):
        self.driver = dealer_session_login
        loc(self.driver).search_name(data["add_name"])
        assert 1 == 0


if __name__ == '__main__':
    pytest.main(['-s', 'test_system.py'])