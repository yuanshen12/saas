from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Receive(BasePage):
    click_subscribe = (By.CLASS_NAME, "el-menu-item")
    click_ly = (By.CLASS_NAME, 'btn_ly')
    click_mc = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[2]/form[2]/div[1]/div/div[3]/table/tbody/tr/td[2]')
    input_name = (By.CLASS_NAME, "el-input__inner")
    click_xz = (By.CLASS_NAME, 'el-table__row')
    click_sava = (By.CLASS_NAME, "normal")

    click_even = (By.CLASS_NAME, "wl-gengduo")
    click_jl = (By.CLASS_NAME, 'el-table__row')
    click_sh = (By.CLASS_NAME, 'btn_sh')
    click_ck = (By.CLASS_NAME, 'btn_ck')
    click_qr = (By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/button')

    def add_ly(self, add_name):
        """
        :param add_name: 商品名称
        :return: 领用申请
        """
        try:
            self.click_element(self.click_subscribe, num=8)
            self.click_element(self.click_subscribe, num=6)
            self.click_element(self.click_ly)
            self.click_element(self.click_mc)
            self.input_element(self.input_name, add_name, num=10)
            self.click_element(self.click_xz, num=-1)
            self.click_element(self.click_sava)
            sleep(2)
        except:
            return False
        else:
            return True

    def add_sh(self):
        """
        :return: 领用审核流程
        """
        even = self.get_element_text(self.click_even)
        if even == "更多":
            self.click_element(self.click_even)
        try:
            self.click_element(self.click_jl, num=0)
            self.click_element(self.click_sh)
            self.click_element(self.click_sava)
            sleep(2)
        except:
            return False
        else:
            return True

    def add_ck(self):
        """
        :return: 领用出库流程
        """
        try:
            self.get_element_rf()
            self.click_element(self.click_ck)
            self.click_element(self.click_jl, num=-1)
            self.click_element(self.click_sava, num=1)
            sleep(2)
            self.click_element(self.click_qr)
            sleep(2)
        except:
            return False
        else:
            return True





