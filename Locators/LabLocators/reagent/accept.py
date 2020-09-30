from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Accept(BasePage):
    click_subscribe = (By.CLASS_NAME, "el-menu-item")
    click_ap = (By.CLASS_NAME, "btn_ys")
    click_jl = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div/form[2]/div/div[1]/div[3]/table/tbody/tr/td[1]')
    click_sava = (By.CLASS_NAME, "normal")

    def add_ap(self):
        """
        :return: 验收入库
        """
        self.click_element(self.click_subscribe, num=8)
        self.click_element(self.click_subscribe, num=4)
        try:
            sleep(2)
            self.click_element(self.click_ap, num=1)
            self.click_element(self.click_jl)
            self.click_element(self.click_sava)
            sleep(2)
        except:
            return False
        else:
            return True
