from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Warehouse(BasePage):

    click_system = (By.CLASS_NAME, "el-menu-item")
    click_ad = (By.CLASS_NAME, 'btn_xz1')
    save = (By.CLASS_NAME, 'normal')
    input_ = (By.CLASS_NAME, 'el-input__inner')
    click_xz = (By.CLASS_NAME, 'el-table__row')
    click_sc = (By.CLASS_NAME, 'btn_sc')
    click_qr = (By.CLASS_NAME, 'el-button--small')

    def get_a(self):
        """
        :return: 新增仓库
        """
        sleep(2)
        self.click_element(self.click_system, num=0)
        self.click_element(self.click_system, num=7)
        try:
            sleep(2)
            self.click_element(self.click_system, num=7)
            self.click_element(self.click_ad)
            self.click_element(self.save)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_b(self, add_name):
        """
        :param add_name: 仓库名称
        :return: 新增仓库
        """
        try:
            self.input_element(self.input_, add_name, num=5)
            self.click_element(self.save)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_c(self):
        """
        :return: 删除仓库
        """
        try:
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_sc)
            self.click_element(self.click_qr, num=-1)
            sleep(2)
        except:
            return False
        else:
            return True

