from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Accept(BasePage):
    click_subscribe = (By.CLASS_NAME, "el-menu-item")
    click_ap = (By.CLASS_NAME, "btn_ys")
    click_jl = (By.CLASS_NAME, "el-tag--mini")
    click_sava = (By.CLASS_NAME, "normal")

    def add_ap(self):
        self.click_element(self.click_subscribe, num=8)
        self.click_element(self.click_subscribe, num=4)
        try:
            self.click_element(self.click_ap, num=1)
            self.click_element(self.click_jl, num=0)
            self.click_element(self.click_sava)
            sleep(2)
        except:
            return False
        else:
            return True
