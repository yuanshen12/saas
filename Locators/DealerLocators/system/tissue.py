from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Tissue(BasePage):

    click_system = (By.CLASS_NAME, "el-menu-item")
    click_dw = (By.CLASS_NAME, 'btn_sysxx')
    click_sh = (By.CLASS_NAME, 'el-radio__inner')
    save = (By.CLASS_NAME, 'normal')
    click_xz = (By.CLASS_NAME, 'btn_xz1')
    input_ = (By.CLASS_NAME, 'el-input__inner')
    click_xq = (By.CLASS_NAME, 'btn_xq')
    click_tx = (By.CLASS_NAME, 'el-textarea__inner')
    click_sc = (By.CLASS_NAME, 'btn_sc')
    click_qr = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span')

    def get_a(self):
        """
        :return: 单位信息设置不需要审核
        """
        self.click_element(self.click_system, num=11)
        self.click_element(self.click_system, num=8)
        try:
            self.click_element(self.click_dw)
            self.click_element(self.click_sh, num=1)
            self.click_element(self.click_sh, num=3)
            self.click_element(self.click_sh, num=5)
            self.click_element(self.save, num=1)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_b(self):
        """
        :return: 单位信息设置需要审核
        """
        try:
            self.click_element(self.click_dw)
            sleep(2)
            self.click_element(self.click_sh, num=0)
            self.click_element(self.click_sh, num=2)
            self.click_element(self.click_sh, num=4)
            self.click_element(self.save, num=1)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_c(self, add_name):
        """
        :param add_name: 部门名称
        :return: 新增部门
        """
        try:
            self.click_element(self.click_xz)
            sleep(1)
            self.input_element(self.input_, add_name, num=2)
            self.click_element(self.save)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_d(self, add_b):
        """
        :param add_b: 这是备注
        :return: 详情修改部门
        """
        try:
            self.click_element(self.click_xq, num=-1)
            sleep(1)
            self.input_element(self.click_tx, add_b, num=1)
            self.click_element(self.save)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_f(self):
        """
        :return: 删除部门
        """
        try:
            self.get_element_rf()
            self.click_element(self.click_sc, num=1)
            self.click_element(self.click_qr)
            sleep(2)
        except:
            return False
        else:
            return True

