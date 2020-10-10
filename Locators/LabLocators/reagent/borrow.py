from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Borrow(BasePage):

    click_subscribe = (By.CLASS_NAME, "el-menu-item")
    click_borrow = (By.CLASS_NAME, "btn_jyck")
    input_name = (By.CLASS_NAME, "el-input__inner")
    click_sp = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div/div[3]/table/tbody/tr/td[2]')
    click_qd = (By.XPATH, '/html/body/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[2]')
    click_sava = (By.CLASS_NAME, "normal")
    click_xz = (By.CLASS_NAME, 'el-table__row')
    click_gh = (By.CLASS_NAME, 'btn_jygh')

    def get_borrow(self, add_name, add_sys, add_sp):
        """
        :param add_name: 借用名称
        :param add_sys: 借用实验室
        :param add_sp: 借用商品
        :return: 借用出库流程
        """
        self.click_element(self.click_subscribe, num=8)
        self.click_element(self.click_subscribe, num=8)
        try:
            self.get_element_rf()
            self.click_element(self.click_borrow)
            self.input_element(self.input_name, add_name, num=6)
            self.input_element(self.input_name, add_sys, num=7)
            self.click_element(self.click_sp)
            self.input_element(self.input_name, add_sp, num=12)
            self.click_element(self.click_qd)
            self.click_element(self.click_sava)
        except:
            return False
        else:
            return True

    def get_give(self):
        """
        :return: 借用归还
        """
        try:
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_gh)
            self.click_element(self.click_sava)
        except:
            return False
        else:
            return True


