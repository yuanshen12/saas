from selenium.webdriver.common.by import By
from Common.plugs.basepage import BasePage
import time


class SubscribeLocators(BasePage):
    click_subscribe = (By.CLASS_NAME, "el-menu-item")
    click_message = (By.CLASS_NAME, "el-button--text")
    click_choose = (By.CLASS_NAME, "el-radio__inner")
    click_save = (By.CLASS_NAME, "normal")

    click_add = (By.CLASS_NAME, "spanIcon")
    input_name = (By.CLASS_NAME, "el-input__inner")
    success_name = (By.CLASS_NAME, "line-height")

    click_ensure = (By.CLASS_NAME, "el-button--small")

    # 开启资金账户
    def get_subscribe(self, choose):
        '''
        :param choose: fend_start开启资金，fend_stop关闭资金
        :return:
        '''
        self.click_element(self.click_subscribe, num=7)
        self.click_element(self.click_message, num=0)
        try:
            if choose == "fend_start":
                self.click_element(self.click_choose, num=0)
                self.click_element(self.click_save, num=1)
            elif choose == "fend_stop":
                self.click_element(self.click_choose, num=1)
                self.click_element(self.click_save, num=1)
        except:
            return False
        else:
            return True

    # 增加项目组
    def get_add_sub(self, add_name):
        self.click_element(self.click_add, num=0)
        self.input_element(self.input_name, add_name, keys_control=0, num=2)
        self.click_element(self.click_save)
        add_text = self.get_element_text(self.success_name, num=4)
        return add_text

    # 项目组详情
    def get_details(self, add_name):
        self.click_element(self.click_add, num=4)
        self.input_element(self.input_name, add_name, keys_control=1, num=2)
        self.click_element(self.click_save)
        time.sleep(1)
        success_text = self.get_element_text(self.success_name, num=4)
        return success_text

    def get_del(self):
        try:
            self.click_element(self.click_add, num=5)
            self.click_element(self.click_ensure, num=1)
        except:
            return False
        else:
            time.sleep(2)
            return True


