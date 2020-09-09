from selenium.webdriver.common.by import By
import time


class SystemLocators():
    click_subscribe = (By.CLASS_NAME, "card_wrap_icon")
    click_system = (By.CLASS_NAME, "el-menu-item")

    def __init__(self, driver):
        self.driver = driver

    def get_system(self):
        self.driver.find_element(*self.click_subscribe).click()
        time.sleep(2)
        self.driver.find_elements(*self.click_system)[12].click()


