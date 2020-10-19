from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Examine(BasePage):

    click_system = (By.CLASS_NAME, "el-menu-item")
    click_xq = (By.CLASS_NAME, 'btn_xq')
    click_xz = (By.CLASS_NAME, 'el-radio__inner')
    save = (By.CLASS_NAME, 'normal')

    def get_a(self, choose=0):
        """
        :return: 订单审核流程
        """
        self.click_element(self.click_system, num=11)
        self.click_element(self.click_system, num=11)
        try:
            if choose == 0:
                self.click_element(self.click_xq, num=0)
            elif choose == 1:
                self.click_element(self.click_xq, num=1)
            elif choose == 2:
                self.click_element(self.click_xq, num=2)
            elif choose == 3:
                self.click_element(self.click_xq, num=3)
            elif choose == 4:
                self.click_element(self.click_xq, num=4)
            self.click_element(self.click_xz, num=1)
            self.click_element(self.click_xz, num=0)
            self.click_element(self.save)
            sleep(1)
        except:
            return False
        else:
            return True