from selenium.webdriver.common.by import By
from Common.plugs.basepage import BasePage


class SystemLocators(BasePage):
    click_subscribe = (By.CLASS_NAME, "card_wrap_icon")
    click_system = (By.CLASS_NAME, "el-menu-item")

    def get_system(self):
        self.click_element(self.click_subscribe)
        self.click_element(self.click_system, num=12)


