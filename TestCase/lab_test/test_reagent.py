import pytest, allure
from Locators.LabLocators.reagent import Reagent as loc
from TestCase.lab_test import lab_datas as LD


class TestSystem():

    @pytest.mark.parametrize("data", LD.add_reagent_name)
    def test_06(self, session_login, data):
        self.driver = session_login
        reagent = loc(self.driver).add_reagent(data["add_name"])
        assert reagent is True

    @pytest.mark.parametrize("data", LD.add_reagent_name)
    def test_07(self, session_login, data):
        self.driver = session_login
        search = loc(self.driver).search_name(data["add_name"])
        assert search == data["add_name"]

    @pytest.mark.parametrize("data", LD.add_reagent_cas)
    def test_08(self, session_login, data):
        self.driver = session_login
        add_go = loc(self.driver).alter_reagent(data["add_cas"])
        assert add_go is True

    @pytest.mark.skip(reason="这是一个BUG！！")
    def test_09(self, session_login):
        self.driver = session_login
        del_ensure = loc(self.driver).del_reagent()
        assert del_ensure is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_reagent.py'])