from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class SubscribeLocators():
    click_subscribe = (By.CLASS_NAME, "el-menu-item")
    click_message = (By.CLASS_NAME, "el-button--text")
    click_choose = (By.CLASS_NAME, "el-radio__inner")
    click_save = (By.CLASS_NAME, "normal")

    click_add = (By.CLASS_NAME, "spanIcon")
    input_name = (By.CLASS_NAME, "el-input__inner")
    success_name = (By.CLASS_NAME, "line-height")

    click_ensure = (By.CLASS_NAME, "el-button--small")

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
        try:
            if choose == "fend_start":
                self.driver.find_elements(*self.click_choose)[0].click()
                self.driver.find_elements(*self.click_save)[1].click()
            elif choose == "fend_stop":
                self.driver.find_elements(*self.click_choose)[1].click()
                self.driver.find_elements(*self.click_save)[1].click()
        except:
            return False
        else:
            time.sleep(1)
            return True

    # 增加项目组
    def get_add_sub(self, add_name):
        self.driver.find_elements(*self.click_add)[0].click()
        self.driver.find_elements(*self.input_name)[2].send_keys(add_name)
        self.driver.find_element(*self.click_save).click()
        time.sleep(2)
        success_text = self.driver.find_elements(*self.success_name)[4].text
        return success_text

    # 项目组详情
    def get_details(self, add_name):
        self.driver.find_elements(*self.click_add)[4].click()
        element_cope = self.driver.find_elements(*self.input_name)[2]
        element_cope.send_keys(Keys.CONTROL, 'a')
        element_cope.send_keys(add_name)
        self.driver.find_element(*self.click_save).click()
        time.sleep(2)
        success_text = self.driver.find_elements(*self.success_name)[4].text
        return success_text

    def get_del(self):
        try:
            self.driver.find_elements(*self.click_add)[5].click()
            self.driver.find_elements(*self.click_ensure)[1].click()
        except:
            return False
        else:
            return True


