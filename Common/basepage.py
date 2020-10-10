from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_vs(self, ec, locator):
        """
        :param ec:
        :param locator: 定位信息
        :return:
        """
        WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(ec(locator))

    def get_element(self, ec, locator, num=None):
        """
        :param ec:
        :param locator: 定位信息
        :param num: 定位元素的复数
        :return:
        """
        try:
            if num is None:
                self.wait_vs(ec, locator)
                return self.driver.find_element(*locator)
            else:
                self.wait_vs(ec, locator)
                return self.driver.find_elements(*locator)[num]
        except:
            raise

    def click_element(self, locator, num=None):
        """
        :param locate: 定位方式
        :param locator: 定位信息
        :param num: 定位元素的复数
        :return:
        """
        try:
            if num is None:
                self.get_element(EC.element_to_be_clickable, locator).click()
            else:
                self.get_element(EC.element_to_be_clickable, locator, num).click()
        except:
            raise

    def input_element(self, locator, keys, keys_control=None, num=None):
        """
        :param locator: 输入元素
        :param keys: 输入的数据信息
        :param keys_control: 全选输入框已经有的信息
        :param num: 元素的复数
        :return:
        """
        try:
            if keys_control is None:
                self.get_element(EC.visibility_of_any_elements_located, locator, num).send_keys(keys)
            elif keys_control == 0:
                self.get_element(EC.visibility_of_any_elements_located, locator, num).send_keys(keys)
            else:
                element_ = self.get_element(EC.visibility_of_any_elements_located, locator, num)
                element_.send_keys(Keys.CONTROL, 'a')
                element_.send_keys(keys)
        except:
            raise

    def get_element_text(self, locator, num=None):
        """
        :param locator: 定位信息
        :param num: 定位元素的复数
        :return:
        """
        try:
            return self.get_element(EC.visibility_of_all_elements_located, locator, num).text
        except:
            raise

    def get_element_rf(self):
        self.driver.refresh()


