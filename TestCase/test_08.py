import pytest, allure
from Locators.LabLocators.system.check import Check as loc_check
from TestCase import lab_datas as LD


class TestSystem():

    @pytest.mark.smoke
    @allure.story("审核流程")
    def test_41(self, session_login):
        self.driver = session_login
        check = loc_check(self.driver).alter_check_yes()
        assert check is True

    @pytest.mark.smoke
    @allure.story("审核流程")
    def test_42(self, session_login):
        self.driver = session_login
        check = loc_check(self.driver).alter_check_no()
        assert check is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_08.py'])