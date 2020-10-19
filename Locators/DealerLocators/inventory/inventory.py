from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Inventory(BasePage):

    click_system = (By.CLASS_NAME, "el-menu-item")
    click_rk = (By.CLASS_NAME, 'btn_rk')
    save = (By.CLASS_NAME, 'normal')
    click_mc = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[2]/div')
    input_ = (By.CLASS_NAME, 'el-input__inner')
    click_ls = (By.CLASS_NAME, 'blue')
    click_sl = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[8]/div')
    click_ck = (By.CLASS_NAME, 'btn_ck')
    click_mc1 = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[2]/div')
    click_qr = (By.XPATH, '/html/body/div[3]/div[1]/div[3]/table/tbody/tr/td[2]/div/div')
    click_bs = (By.CLASS_NAME, 'btn_bs')
    input_1 = (By.CLASS_NAME, 'el-textarea__inner')
    click_mc2 = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[2]/div')
    click_qr1 = (By.XPATH, '/html/body/div[3]/div[1]/div[3]/table/tbody/tr[2]/td[2]/div/div')
    click_ss = (By.CLASS_NAME, 'el-input__inner')
    click_sss = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/form/div/div/div[2]/div/div/button')
    click_xq = (By.CLASS_NAME, 'btn_xq')
    click_gk = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div/div[2]/div[4]/div[1]/form[1]/div[20]/div/div[2]/div/div/div[1]')
    click_gks = (By.XPATH, '/html/body/div[8]/div[1]/div[1]/ul/li[1]')

    def get_a(self):
        """
        :return: 直接入库
        """
        self.click_element(self.click_system, num=0)
        self.click_element(self.click_system, num=7)
        try:
            sleep(2)
            self.click_element(self.click_system, num=4)
            self.click_element(self.click_rk)
            self.click_element(self.save)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_b(self, add_name, add_num):
        """
        :param add_name: 入库商品
        :param add_num: 入库数量
        :return: 直接入库
        """
        try:
            self.click_element(self.click_mc)
            self.input_element(self.input_, add_name, num=11)
            self.click_element(self.click_ls, num=0)
            self.click_element(self.click_sl)
            self.input_element(self.input_, add_num, num=11)
            self.click_element(self.save)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_c(self):
        """
        :param add_name: 商品名称
        :param add_num: 出库数量
        :return: 直接出库
        """
        try:
            self.get_element_rf()
            self.click_element(self.click_ck)
            self.click_element(self.click_mc1)
            self.click_element(self.click_qr)
            self.click_element(self.save, num=-1)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_d(self, add_name):
        """
        :param add_name: 商品名称
        :return: 报损商品
        """
        try:
            self.get_element_rf()
            self.click_element(self.click_bs)
            self.input_element(self.input_1, add_name, num=1)
            self.click_element(self.click_mc2)
            self.click_element(self.click_qr1)
            self.click_element(self.save, num=-1)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_e(self, add_name):
        """
        :param add_name: 商品名称
        :return: 搜索
        """
        try:
            self.input_element(self.input_, add_name, num=5)
            self.click_element(self.click_sss)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_f(self):
        """
        :return: 修改为公开商品
        """
        try:
            self.click_element(self.click_xq, num=0)
            self.click_element(self.click_gk)
            self.click_element(self.click_gks)
            self.click_element(self.save)
            sleep(2)
        except:
            return False
        else:
            return True




