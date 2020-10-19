from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Purchase(BasePage):

    click_system = (By.CLASS_NAME, "el-menu-item")
    click_ad = (By.CLASS_NAME, 'btn_xz1')
    input_ = (By.CLASS_NAME, 'el-input__inner')
    save = (By.CLASS_NAME, 'normal')
    click_mc = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[3]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[2]/div')
    click_ls = (By.CLASS_NAME, 'blue')
    click_sl = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[3]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[8]/div')
    click_xz = (By.CLASS_NAME, 'el-table__row')
    click_xd = (By.CLASS_NAME, 'btn_xd')
    click_cx = (By.CLASS_NAME, 'btn_back')
    click_qr = (By.CLASS_NAME, 'el-button--small')
    click_sh = (By.CLASS_NAME, 'btn_sh')
    click_bt = (By.CLASS_NAME, 'el-radio__inner')
    click_xj = (By.CLASS_NAME, 'xj')
    click_mc1 = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[2]/div')
    click_sl1 = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[7]/div')
    click_gys = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/form/div/div[2]/div/div[1]/form[1]/div[4]/div/div[2]/div/div[1]/div[2]')
    click_gys1 = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li')
    click_gb = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/button[1]')
    click_ss = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/form/div/div/div[2]/div/div')
    click_gb1 = (By.CLASS_NAME, 'el-message-box__close')

    def get_a(self):
        """
        :return: 申购流程
        """
        self.click_element(self.click_system, num=0)
        self.click_element(self.click_system, num=6)
        try:
            sleep(2)
            self.click_element(self.click_ad)
            self.click_element(self.save, num=1)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_b(self, add_name, add_names, add_num, choose=None):
        """
        :param choose: 选择采购新增
        :param add_name: 供应商名称
        :param add_names: 商品名称
        :param add_num: 商品数量
        :return: 采购流程
        """
        try:
            if choose is not None:
                self.click_element(self.click_ad)
            self.input_element(self.input_, add_name, num=6)
            self.click_element(self.click_mc)
            self.input_element(self.input_, add_names, num=24)
            self.click_element(self.click_ls, num=-1)
            self.click_element(self.click_sl)
            self.input_element(self.input_, add_num, num=24)
            self.click_element(self.save, num=1)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_c(self, add_name):
        """
        :return: 从申购进行采购
        """
        try:
            self.click_element(self.click_ad)
            self.click_element(self.save, num=0)
            sleep(2)
            self.click_element(self.click_xz, num=-1)
            self.input_element(self.input_, add_name, num=6)
            self.click_element(self.save, num=3)
            self.click_element(self.save, num=2)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_d(self):
        """
        :return: 选择审核中订单撤销
        """
        try:
            self.click_element(self.click_xz, num=1)
            self.click_element(self.click_cx)
            self.click_element(self.click_qr, num=-1)
            sleep(1)
        except:
            return False
        else:
            return True

    def get_f(self):
        """
        :return: 选择订单下单
        """
        try:
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_xz, num=2)
            self.click_element(self.click_xd)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_g(self):
        """
        :return: 采购审核通过
        """
        try:
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_sh)
            self.click_element(self.save)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_h(self):
        """
        :return: 采购审核不通过
        """
        try:
            self.click_element(self.click_xz, num=2)
            self.click_element(self.click_sh)
            self.click_element(self.click_bt, num=1)
            self.click_element(self.save)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_j(self, add_mc, add_sl):
        """
        :param add_mc: 询价商品名称
        :param add_sl: 询价商品数量
        :return: 询价商品
        """
        try:
            self.get_element_rf()
            self.click_element(self.click_xj)
            self.click_element(self.save, num=-1)
            sleep(2)
            self.click_element(self.click_gys)
            self.click_element(self.click_gys1)
            self.click_element(self.click_mc1)
            self.input_element(self.input_, add_mc, num=15)
            self.click_element(self.click_sl1)
            self.input_element(self.input_, add_sl, num=15)
            self.click_element(self.save, num=-1)
            sleep(2)
            self.click_element(self.click_gb)
            sleep(2)
            self.click_element(self.click_gb1)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_k(self, add_name):
        """
        :param add_name: 搜索名称
        :return: 搜索
        """
        try:
            self.input_element(self.input_, add_name, num=3)
            self.click_element(self.click_ss)
            sleep(2)
        except:
            return False
        else:
            return True










