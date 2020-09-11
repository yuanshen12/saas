from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 显示等待元素出现
    def wait_vs(self, locator):
        WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_any_elements_located(locator))

    # 查找元素
    def get_element(self, locator, num=None):
        try:
            if num is None:
                self.wait_vs(locator)
                return self.driver.find_element(*locator)
            else:
                self.wait_vs(locator)
                return self.driver.find_elements(*locator)[num]
        except:
            raise

    # 点击操作
    def click_element(self, locator, num=None):
        try:
            self.wait_vs(locator)
            self.get_element(locator, num).click()
        except:
            raise

    # 输入操作
    def input_element(self, locator, keys, keys_control=None, num=None):
        '''
        :param locator: 输入元素
        :param keys: 输入的数据信息
        :param keys_control: 全选输入框已经有的信息
        :param num: 元素的复数
        :return:
        '''
        try:
            if keys_control is None:
                self.wait_vs(locator)
                self.get_element(locator, num).send_keys(keys)
            elif keys_control == 0:
                self.get_element(locator, num).send_keys(keys)
            else:
                element_ = self.get_element(locator, num)
                element_.send_keys(Keys.CONTROL, 'a')
                element_.send_keys(keys)
        except:
            raise

    # 获取文本
    def get_element_text(self, locator, num=None):
        try:
            self.wait_vs(locator)
            return self.get_element(locator, num).text
        except:
            raise

