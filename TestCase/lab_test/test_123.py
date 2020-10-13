import pytest, allure
from Locators.LabLocators.system.member import Member as loc
from TestCase.lab_test import lab_datas as LD


class TestSystem():

    @pytest.mark.parametrize("data", LD.add_c)
    def test_18(self, session_login, data):
        self.driver = session_login
        br = loc(self.driver).add_m(data['add_user'], data['add_name'])
        assert br is True

    def test_19(self, session_login):
        self.driver = session_login
        br = loc(self.driver).get_t()
        assert br is True

    def test_20(self, session_login):
        self.driver = session_login
        br = loc(self.driver).get_q()
        assert br is True

    @pytest.mark.parametrize("data", LD.add_c)
    def test_22(self, session_login, data):
        self.driver = session_login
        br = loc(self.driver).get_ss(data['add_name'])
        assert br is True

    def test_23(self, session_login):
        self.driver = session_login
        br = loc(self.driver).get_z()
        assert br is True

    def test_24(self, session_login):
        self.driver = session_login
        br = loc(self.driver).get_s()
        assert br is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_123.py'])