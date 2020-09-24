from selenium.webdriver.common.by import By
from Common.plugs.basepage import BasePage
from time import sleep


class SystemLocators(BasePage):

    click_system = (By.CLASS_NAME, "el-menu-item")

    def system_tissue(self):
        try:
            self.click_element(self.click_system, num=11)
            sleep(5)
            return True
        except:
            return False