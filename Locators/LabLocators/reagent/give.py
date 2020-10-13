from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Give(BasePage):

    click_subscribe = (By.CLASS_NAME, "el-menu-item")
    click_xz = (By.CLASS_NAME, 'el-table__row')
    click_gh = (By.CLASS_NAME, 'btn_gh')
    click_sava = (By.CLASS_NAME, "normal")

    def add_give(self):
        """
        :return: 借用归还流程
        """
        self.click_element(self.click_subscribe, num=8)
        self.click_element(self.click_subscribe, num=7)
        try:
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_gh)
            self.click_element(self.click_sava)
            sleep(2)
        except:
            return False
        else:
            return True

