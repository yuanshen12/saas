import pytest, allure
from Locators.LabLocators.reagent.check import Check as loc
from TestCase.lab_test import lab_datas as LD


class TestSystem():

    # @pytest.mark.parametrize("data", LD.add_br_name)
    # def test_18(self, session_login, data):
    #     self.driver = session_login
    #     br = loc(self.driver).get_borrow(data['add_name'], data['add_sys'], data['add_sp'])
    #     assert br is True

    def test_19(self, session_login):
        self.driver = session_login
        ck = loc(self.driver).add_ck()
        assert ck is True

    def test_21(self, session_login):
        self.driver = session_login
        ck = loc(self.driver).add_tj()
        assert ck is True

    def test_22(self, session_login):
        self.driver = session_login
        ck = loc(self.driver).add_sh()
        assert ck is True

    def test_23(self, session_login):
        self.driver = session_login
        ck = loc(self.driver).add_cl()
        assert ck is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_123.py'])