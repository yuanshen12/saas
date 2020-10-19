from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Stocking(BasePage):

    click_system = (By.CLASS_NAME, "el-menu-item")
    save = (By.CLASS_NAME, 'normal')
    click_ad = (By.CLASS_NAME, 'btn_xz1')
    click_sd = (By.CLASS_NAME, 'wl-icon-container1')
    click_xz = (By.CLASS_NAME, 'el-table__row')
    click_tj = (By.CLASS_NAME, 'btn_tj')
    click_sh = (By.CLASS_NAME, 'btn_sh')
    click_cl = (By.CLASS_NAME, 'btn_cl')
    input_ = (By.CLASS_NAME, 'el-input__inner')
    click_qr = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/form/div/div/div[2]/div/div/button')

    def get_a(self):
        """
        :return: 新增盘点
        """
        self.click_element(self.click_system, num=0)
        self.click_element(self.click_system, num=7)
        try:
            sleep(2)
            self.click_element(self.click_system, num=5)
            self.click_element(self.click_ad)
            self.click_element(self.save)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_b(self):
        """
        :return: 新增盘点
        """
        try:
            self.click_element(self.click_sd)
            self.click_element(self.save)
            sleep(3)
        except:
            return False
        else:
            return True

    def get_c(self):
        """
        :return: 盘点提交
        """
        try:
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_tj)
            sleep(3)
        except:
            return False
        else:
            return True

    def get_d(self):
        """
        :return: 盘点审核
        """
        try:
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_sh)
            self.click_element(self.save)
            sleep(3)
        except:
            return False
        else:
            return True

    def get_e(self):
        """
        :return: 盈亏处理
        """
        try:
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_cl)
            sleep(3)
        except:
            return False
        else:
            return True

    def get_f(self, add_name):
        """
        :param add_name: 仓库名称
        :return: 默认仓库盈亏处理
        """
        try:
            self.input_element(self.input_, add_name, num=3)
            self.click_element(self.click_qr)
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_cl)
            sleep(3)
        except:
            return False
        else:
            return True


