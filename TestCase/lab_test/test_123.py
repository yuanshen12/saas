import pytest, allure
from Locators.LabLocators.reagent.accept import Accept as loc
from TestCase.lab_test import lab_datas as LD


class TestSystem():

    def test_6(self, session_login):
        self.driver = session_login
        pc = loc(self.driver).add_ap()
        assert pc is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_123.py'])