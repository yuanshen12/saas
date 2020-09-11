import pytest
from Common.common_auth import Auth
from TestDatas.LoginDatas import login_datas as LD
from Locators.LoginLocators.login_locators import LoginLocators as loc


class TestLogin():

    @pytest.mark.parametrize('data', LD.error_username_data)
    def test_01(self, start_module, data):
        self.driver = start_module
        auth = Auth(self.driver).auth_all('../img/img_03.png')
        loc(self.driver).get_login(data["username"], data["password"], auth)
        try:
            assert loc(self.driver).get_error_username() == data["errorMsg"]
        except:
            raise

    @pytest.mark.parametrize('data', LD.error_password_data)
    def test_02(self, start_module, data):
        self.driver = start_module
        auth = Auth(self.driver).auth_all('../img/img_03.png')
        loc(self.driver).get_login(data["username"], data["password"], auth)
        try:
            assert loc(self.driver).get_error_password() == data["errorMsg"]
        except:
            raise

    @pytest.mark.parametrize("data", LD.success_data)
    def test_03(self, start_module, data):
        self.driver = start_module
        auth = Auth(self.driver).auth_all('../img/img_03.png')
        loc(self.driver).get_login(data["username"], data["password"], auth)
        try:
            assert "欢迎您" in loc(self.driver).get_login_success()
        except:
            raise


if __name__ == '__main__':
    pytest.main(['-s', 'login_test.py'])
