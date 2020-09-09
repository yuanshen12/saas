from selenium.webdriver.common.by import By
import time


class SubscribeLocators():
    click_subscribe = (By.CLASS_NAME, "el-menu-item")
    click_message = (By.CLASS_NAME, "el-button--text")
    click_choose = (By.CLASS_NAME, "el-radio__inner")
    click_save = (By.CLASS_NAME, "normal")

    click_add = (By.CLASS_NAME, "spanIcon")

    def __init__(self, driver):
        self.driver = driver

    # 开启资金账户
    def get_subscribe(self, choose):
        '''
        :param choose: fend_start开启资金，fend_stop关闭资金
        :return:
        '''
        time.sleep(2)
        self.driver.find_elements(*self.click_subscribe)[7].click()
        self.driver.find_elements(*self.click_message)[0].click()
        if choose == "fend_start":
            self.driver.find_elements(*self.click_choose)[0].click()
            self.driver.find_elements(*self.click_save)[1].click()
        elif choose == "fend_stop":
            self.driver.find_elements(*self.click_choose)[1].click()
            self.driver.find_elements(*self.click_save)[1].click()
        time.sleep(5)

    # 增加项目组
    def get_add_sub(self):
        self.driver.find_elements(*self.click_add)[0].click()

