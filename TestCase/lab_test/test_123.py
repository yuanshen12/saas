import pytest, allure
from Locators.LabLocators.reagent.receive import Receive as loc
from TestCase.lab_test import lab_datas as LD


class TestSystem():

    @pytest.mark.parametrize("data", LD.add_rk_name)
    def test_18(self, session_login, data):
        self.driver = session_login
        rt = loc(self.driver).add_ly(data['add_name'])
        assert rt is True

    def test_19(self, session_login):
        self.driver = session_login
        sh = loc(self.driver).add_sh()
        assert sh is True

    def test_20(self, session_login):
        self.driver = session_login
        ck = loc(self.driver).add_ck()
        assert ck is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_123.py'])