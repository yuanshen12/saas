import pytest, allure
from Locators.LabLocators.system.reagent import Reagent as loc_reagent
from TestCase import lab_datas as LD


class TestSystem():

    @allure.story("试剂耗材信息")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_reagent_name)
    def test_22(self, session_login, data):
        self.driver = session_login
        reagent = loc_reagent(self.driver).add_reagent(data["add_1"])
        assert reagent is True

    @allure.story("试剂耗材信息")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_reagent_name)
    def test_23(self, session_login, data):
        self.driver = session_login
        search = loc_reagent(self.driver).search_name(data["add"])
        assert search is True

    @allure.story("试剂耗材信息")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_reagent_cas)
    def test_24(self, session_login, data):
        self.driver = session_login
        add_go = loc_reagent(self.driver).alter_reagent(data["add_cas"])
        assert add_go is True

    @allure.story("试剂耗材信息")
    @pytest.mark.smoke
    def test_25(self, session_login):
        self.driver = session_login
        del_ensure = loc_reagent(self.driver).get_a()
        assert del_ensure is True

    @allure.story("试剂耗材信息")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_reagent_name)
    def test_26(self, session_login, data):
        self.driver = session_login
        del_ensure = loc_reagent(self.driver).get_b(data["add_2"], data['add_num'])
        assert del_ensure is True

    @allure.story("试剂耗材信息")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_reagent_name)
    def test_27(self, session_login, data):
        self.driver = session_login
        del_ensure = loc_reagent(self.driver).get_c(data['num_1'])
        assert del_ensure is True

    @allure.story("试剂耗材信息")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", LD.add_reagent_name)
    def test_28(self, session_login, data):
        self.driver = session_login
        del_ensure = loc_reagent(self.driver).get_d(data['num_1'])
        assert del_ensure is True

    @allure.story("试剂耗材信息")
    @pytest.mark.smoke
    def test_29(self, session_login):
        self.driver = session_login
        del_ensure = loc_reagent(self.driver).del_reagent()
        assert del_ensure is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_04.py'])