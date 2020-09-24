from selenium.webdriver.common.by import By
from Common.plugs.basepage import BasePage
from time import sleep
import re


class ReagentLocators(BasePage):

    click_reagent = (By.CLASS_NAME, "el-menu-item")
    click_add_reagent = (By.CLASS_NAME, "btn_xz1")
    input_add_name = (By.CLASS_NAME, "el-input__inner")
    click_add_type = (By.CLASS_NAME, "el-cascader__label")
    click_type_ensure = (By.CLASS_NAME, "el-cascader-menu__item")
    click_save = (By.CLASS_NAME, "normal")

    input_search_reagent = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/form/div/div/div[2]/div/input')
    click_search_ensure = (By.CLASS_NAME, "el-input-group__append")
    click_normal = (By.CLASS_NAME, "svg-normal")

    def add_reagent(self, add_name):
        self.click_element(self.click_reagent, num=9)
        try:
            self.click_element(self.click_add_reagent)
            self.input_element(self.input_add_name, add_name, num=5)
            self.click_element(self.click_add_type)
            self.click_element(self.click_type_ensure)
            self.click_element(self.click_save, num=0)
        except:
            return False
        else:
            return True

    def search_name(self, add_name):
        self.click_element(self.input_search_reagent)
        self.input_element(self.input_search_reagent, add_name)
        self.click_element(self.click_search_ensure, num=1)
        self.click_element(self.click_normal, num=2)
        sleep(5)





