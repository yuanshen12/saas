from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Repertory(BasePage):
    click_subscribe = (By.CLASS_NAME, "el-menu-item")
    click_rk = (By.CLASS_NAME, 'btn_rk')
    click_mc = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div/form[2]/div/div[1]/div[3]/table/tbody/tr/td[2]')
    input_name = (By.CLASS_NAME, "el-input__inner")
    click_c = (By.CLASS_NAME, 'blue')
    click_sl = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div/form[2]/div/div[1]/div[3]/table/tbody/tr/td[8]')
    click_sava = (By.CLASS_NAME, "normal")

    click_ck = (By.CLASS_NAME, 'btn_ck')

    click_search = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/form/div/div/div[2]/div/div')
    click_st = (By.CLASS_NAME, 'table-column-label')

    click_even = (By.CLASS_NAME, "wl-gengduo")
    click_cz = (By.CLASS_NAME, 'no-event')
    click_bs = (By.CLASS_NAME, 'btn_bs')
    click_ly = (By.CLASS_NAME, 'el-textarea__inner')

    click_sh = (By.CLASS_NAME, 'btn_sh')
    click_qx = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div[1]/div[2]/table/thead/tr/th[1]')
    click_qd = (By.CLASS_NAME, 'wl-public-btn-close')

    def add_rt(self, add_name, add_num):
        """
        :param add_name: 商品名称
        :param add_num: 商品数量
        :return: 入库流程
        """
        try:
            self.click_element(self.click_subscribe, num=8)
            self.click_element(self.click_subscribe, num=5)
            self.click_element(self.click_rk)
            self.click_element(self.click_mc)
            self.input_element(self.input_name, add_name, num=8)
            self.click_element(self.click_c, num=0)
            self.click_element(self.click_sl)
            self.input_element(self.input_name, add_num, num=8)
            self.click_element(self.click_sava, num=1)
            sleep(2)
        except:
            return False
        else:
            return True

    def search_sp(self, add_name):
        """
        :param add_name: 商品名称
        :return: 搜索商品
        """
        self.input_element(self.input_name, add_name, num=5)
        self.click_element(self.click_search)
        sp_text = self.get_element_text(self.click_st, num=0)
        return sp_text

    def add_ck(self):
        """
        :param add_name: 商品名称
        :return: 出库流程
        """
        try:
            self.click_element(self.click_cz, num=0)
            self.click_element(self.click_ck)
            self.click_element(self.click_sava, num=1)
            sleep(2)
        except:
            return False
        else:
            return True

    def add_bs(self, add_name):
        """
        :param add_name: 报损理由
        :return: 报损流程
        """
        even = self.get_element_text(self.click_even)
        if even == "更多":
            self.click_element(self.click_even)
        try:
            self.click_element(self.click_search)
            self.click_element(self.click_cz, num=0)
            self.click_element(self.click_bs)
            self.input_element(self.click_ly, add_name, num=1)
            self.click_element(self.click_sava)
            sleep(2)
        except:
            return False
        else:
            return True

    def add_sh(self):
        """
        :return: 审核报损流程
        """
        try:
            self.click_element(self.click_sh)
            self.click_element(self.click_qx)
            self.click_element(self.click_sava, num=1)
            self.click_element(self.click_sava, num=2)
            self.click_element(self.click_qd)
            sleep(2)
        except:
            return False
        else:
            return True



