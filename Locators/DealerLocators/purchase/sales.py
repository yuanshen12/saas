from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Sales(BasePage):

    click_system = (By.CLASS_NAME, "el-menu-item")
    click_xz = (By.CLASS_NAME, 'el-table__row')
    click_th = (By.CLASS_NAME, 'btn_bs')
    save = (By.CLASS_NAME, 'normal')

    def get_a(self):
        """
        :return: 申购流程
        """
        self.click_element(self.click_system, num=0)
        self.click_element(self.click_system, num=6)
        try:
            sleep(2)
            self.click_element(self.click_system, num=4)
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_th, num=0)
            self.click_element(self.save)
            sleep(2)
        except:
            return False
        else:
            return True