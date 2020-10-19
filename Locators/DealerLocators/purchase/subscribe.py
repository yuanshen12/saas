from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Subscribe(BasePage):

    click_system = (By.CLASS_NAME, "el-menu-item")
    click_ad = (By.CLASS_NAME, 'btn_xz1')
    save = (By.CLASS_NAME, 'normal')
    click_mz = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[2]/div')
    input_ = (By.CLASS_NAME, 'el-input__inner')
    click_sl = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[10]/div')
    click_xz = (By.CLASS_NAME, 'el-table__row')
    click_tj = (By.CLASS_NAME, 'btn_tj')
    click_sh = (By.CLASS_NAME, 'btn_sh')
    click_bt = (By.CLASS_NAME, 'el-radio__inner')
    click_cx = (By.CLASS_NAME, 'btn_back')
    click_sc = (By.CLASS_NAME, 'btn_sc')
    click_qr = (By.CLASS_NAME, 'el-button--small')

    def get_a(self):
        """
        :return: 申购流程
        """
        self.click_element(self.click_system, num=0)
        self.click_element(self.click_system, num=6)
        sleep(2)
        self.click_element(self.click_system, num=2)
        try:
            self.click_element(self.click_ad)
            self.click_element(self.save, num=0)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_b(self, add_name, add_num):
        """
        :param add_name: 申购商品
        :param add_num: 申购数量
        :return: 申购流程
        """
        self.click_element(self.click_mz)
        self.input_element(self.input_, add_name, num=8)
        self.click_element(self.click_sl)
        self.input_element(self.input_, add_num, num=8)
        try:

            self.click_element(self.save, num=0)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_c(self, add_name, add_num):
        """
        :param add_name: 申购商品
        :param add_num: 申购数量
        :return: 申购流程保存并提交
        """
        try:
            self.click_element(self.click_ad)
            self.click_element(self.click_mz)
            self.input_element(self.input_, add_name, num=8)
            self.click_element(self.click_sl)
            self.input_element(self.input_, add_num, num=8)
            self.click_element(self.save, num=1)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_d(self):
        """
        :return: 申购提交
        """
        try:
            self.click_element(self.click_xz, num=1)
            self.click_element(self.click_tj)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_cd(self):
        """
        :return: 申购商品撤销提交
        """
        try:
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_cx)
            sleep(1)
            self.click_element(self.click_qr, num=1)
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_tj)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_e(self):
        """
        :return: 申购商品审核通过
        """
        try:
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_sh)
            self.click_element(self.save, num=0)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_f(self):
        """
        :return: 申购商品审核不通过
        """
        try:
            self.click_element(self.click_xz, num=1)
            self.click_element(self.click_sh)
            self.click_element(self.click_bt, num=1)
            self.click_element(self.save, num=0)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_h(self):
        """
        :return: 删除申购商品
        """
        try:
            self.click_element(self.click_xz, num=1)
            self.click_element(self.click_sc)
            self.click_element(self.click_qr, num=1)
            sleep(2)
        except:
            return False
        else:
            return True

