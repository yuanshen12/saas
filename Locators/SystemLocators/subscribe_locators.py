from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Common.plugs.basepage import BasePage


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
        print(*self.input_name, add_name)
        # self.driver.find_elements(*self.input_name)[2].send_keys(add_name)

        self.input_element(self.input_name, add_name, keys_control=0, num=2)
        self.click_element(self.click_save)
        add_text = self.get_element_text(self.success_name, num=4)
        # self.driver.find_elements(*self.click_add)[0].click()
        # self.driver.find_elements(*self.input_name)[2].send_keys(add_name)
        # self.driver.find_element(*self.click_save).click()
        # success_text = self.driver.find_elements(*self.success_name)[4].text
        return add_text

    # 项目组详情
    def get_details(self, add_name):
        self.driver.find_elements(*self.click_add)[4].click()
        element_cope = self.driver.find_elements(*self.input_name)[2]
        element_cope.send_keys(Keys.CONTROL, 'a')
        element_cope.send_keys(add_name)
        self.driver.find_element(*self.click_save).click()
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


