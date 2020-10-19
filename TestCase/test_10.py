import pytest, allure
from Locators.LabLocators.reagent.subscribe import Subscribe as loc
from Locators.LabLocators.reagent.purchase import Purchase as loc_pc
from Locators.LabLocators.reagent.accept import Accept as loc_ap
from Locators.LabLocators.reagent.repertory import Repertory as loc_sp
from Locators.LabLocators.reagent.receive import Receive as loc_rc
from Locators.LabLocators.reagent.borrow import Borrow as loc_br
from Locators.LabLocators.reagent.give import Give as loc_gr
from Locators.LabLocators.reagent.check import Check as loc_ck
from TestCase import lab_datas as LD


class TestReagent():

    @pytest.mark.smoke
    @allure.story("申购流程")
    @pytest.mark.parametrize("data", LD.add_su_name)
    def test_43(self, session_login, data):
        self.driver = session_login
        add_su = loc(self.driver).add_su(data['add_name'], data["add_sum"])
        assert add_su is True

    @pytest.mark.smoke
    @allure.story("申购流程")
    @pytest.mark.parametrize("data", LD.add_su_name)
    def test_44(self, session_login, data):
        self.driver = session_login
        su_text = loc(self.driver).search_su(data['add_name'])
        assert su_text == data['add_name']

    @pytest.mark.smoke
    @allure.story("申购流程")
    def test_45(self, session_login):
        self.driver = session_login
        check = loc(self.driver).check_su()
        assert check is True

    @pytest.mark.smoke
    @allure.story("申购流程")
    def test_46(self, session_login):
        self.driver = session_login
        check = loc(self.driver).check_su(choose=1, num=1)
        assert check is True

    @pytest.mark.smoke
    @allure.story("申购流程")
    def test_47(self, session_login):
        self.driver = session_login
        del_ = loc(self.driver).del_su()
        assert del_ is True

    @pytest.mark.smoke
    @allure.story("采购流程")
    @pytest.mark.parametrize("data", LD.add_pc_name)
    def test_48(self, session_login, data):
        self.driver = session_login
        pc = loc_pc(self.driver).add_pc(data['m_name'], data['s_name'])
        assert pc is True

    @pytest.mark.smoke
    @allure.story("采购流程")
    @pytest.mark.parametrize("data", LD.add_pc_name)
    def test_49(self, session_login, data):
        self.driver = session_login
        pc = loc_pc(self.driver).search_pc(data['s_name'])
        assert pc == data['s_name']

    @pytest.mark.smoke
    @allure.story("采购流程")
    def test_50(self, session_login):
        self.driver = session_login
        place = loc_pc(self.driver).place_pc()
        assert place is True

    @pytest.mark.smoke
    @allure.story("采购流程")
    def test_51(self, session_login):
        self.driver = session_login
        place = loc_pc(self.driver).check_pc()
        assert place is True

    @pytest.mark.smoke
    @allure.story("采购流程")
    def test_52(self, session_login):
        self.driver = session_login
        place = loc_pc(self.driver).check_pc(choose=1)
        assert place is True

    @pytest.mark.smoke
    @allure.story("采购流程")
    @pytest.mark.skip("这是个问题！！")
    @pytest.mark.parametrize("data", LD.add_su_name)
    def test_53(self, session_login, data):
        self.driver = session_login
        enquiry = loc_pc(self.driver).enquiry_pc(data['add_name'], data['add_sum'])
        assert enquiry is True

    @pytest.mark.smoke
    @allure.story("验收入库")
    def test_54(self, session_login):
        self.driver = session_login
        pc = loc_ap(self.driver).add_ap()
        assert pc is True

    @pytest.mark.smoke
    @allure.story("库存")
    @pytest.mark.parametrize("data", LD.add_rk_name)
    def test_55(self, session_login, data):
        self.driver = session_login
        rt = loc_sp(self.driver).add_rt(data['add_name'], data['add_sum'])
        assert rt is True

    @pytest.mark.smoke
    @allure.story("库存")
    @pytest.mark.parametrize("data", LD.add_rk_name)
    def test_56(self, session_login, data):
        self.driver = session_login
        sp = loc_sp(self.driver).search_sp(data['add_name'])
        assert sp == data['add_name']

    @pytest.mark.smoke
    @allure.story("库存")
    @pytest.mark.parametrize("data", LD.add_rk_name)
    def test_57(self, session_login, data):
        self.driver = session_login
        ck = loc_sp(self.driver).add_ck()
        assert ck is True

    @pytest.mark.smoke
    @allure.story("库存")
    @pytest.mark.parametrize("data", LD.add_bs_ly)
    def test_58(self, session_login, data):
        self.driver = session_login
        bs = loc_sp(self.driver).add_bs(data['add_name'])
        assert bs is True

    @pytest.mark.smoke
    @allure.story("库存")
    def test_59(self, session_login):
        self.driver = session_login
        sh = loc_sp(self.driver).add_sh()
        assert sh is True

    @pytest.mark.smoke
    @allure.story("库存")
    @pytest.mark.parametrize("data", LD.add_rk_name)
    def test_60(self, session_login, data):
        self.driver = session_login
        xg = loc_sp(self.driver).add_xg(data['add_name'])
        assert xg is True

    @pytest.mark.smoke
    @allure.story("领用")
    @pytest.mark.parametrize("data", LD.add_rk_name)
    def test_61(self, session_login, data):
        self.driver = session_login
        rt = loc_rc(self.driver).add_ly(data['add_name'])
        assert rt is True

    @pytest.mark.smoke
    @allure.story("领用")
    def test_62(self, session_login):
        self.driver = session_login
        sh = loc_rc(self.driver).add_sh()
        assert sh is True

    @pytest.mark.smoke
    @allure.story("领用")
    def test_63(self, session_login):
        self.driver = session_login
        ck = loc_rc(self.driver).add_ck()
        assert ck is True

    @pytest.mark.smoke
    @allure.story("领用归还")
    def test_64(self, session_login):
        self.driver = session_login
        gh = loc_gr(self.driver).add_give()
        assert gh is True

    @pytest.mark.smoke
    @allure.story("借用出库")
    @pytest.mark.parametrize("data", LD.add_br_name)
    def test_65(self, session_login, data):
        self.driver = session_login
        br = loc_br(self.driver).get_borrow(data['add_name'], data['add_sys'], data['add_sp'])
        assert br is True

    @pytest.mark.smoke
    @allure.story("借用出库")
    def test_66(self, session_login):
        self.driver = session_login
        gh = loc_br(self.driver).get_give()
        assert gh is True

    @pytest.mark.smoke
    @allure.story("盘点")
    def test_67(self, session_login):
        self.driver = session_login
        ck = loc_ck(self.driver).add_ck()
        assert ck is True

    @pytest.mark.smoke
    @allure.story("盘点")
    def test_68(self, session_login):
        self.driver = session_login
        ck = loc_ck(self.driver).add_tj()
        assert ck is True

    @pytest.mark.smoke
    @allure.story("盘点")
    def test_69(self, session_login):
        self.driver = session_login
        ck = loc_ck(self.driver).add_sh()
        assert ck is True

    @pytest.mark.smoke
    @allure.story("盘点")
    def test_70(self, session_login):
        self.driver = session_login
        ck = loc_ck(self.driver).add_cl()
        assert ck is True


if __name__ == '__main__':
    pytest.main(['-s', 'test_11.py'])