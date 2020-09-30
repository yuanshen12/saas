from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Reagent(BasePage):

    click_reagent = (By.CLASS_NAME, "el-menu-item")
    click_add_reagent = (By.CLASS_NAME, "btn_xz1")
    input_add_name = (By.CLASS_NAME, "el-input__inner")
    click_add_type = (By.CLASS_NAME, "el-cascader__label")
    click_type_ensure = (By.CLASS_NAME, "el-cascader-menu__item")
    click_save = (By.CLASS_NAME, "normal")

    input_search_reagent = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/form/div/div/div[2]/div/input')
    click_search_ensure = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/form/div/div/div[2]/div/div')
    text_search = (By.CLASS_NAME, "table-column-label")

    click_normal = (By.CLASS_NAME, 'btn_xq')
    click_close = (By.CLASS_NAME, "el-message-box__close")
    click_record = (By.CLASS_NAME, "no-event")
    click_del = (By.CLASS_NAME, "btn_sc")
    click_del_ensure = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div/div[5]/button[2]')

    def add_reagent(self, add_name):
        """
        :param add_name:
        :return: 新增耗材试剂
        """
        sleep(2)
        self.click_element(self.click_reagent, num=9)
        try:
            self.click_element(self.click_add_reagent)
            self.input_element(self.input_add_name, add_name, num=5)
            sleep(1)
            self.click_element(self.click_add_type)
            self.click_element(self.click_type_ensure)
            self.click_element(self.click_save, num=0)
        except:
            return False
        else:
            return True

    def search_name(self, add_name):
        """
        :param add_name:
        :return: 搜索耗材试剂
        """
        self.click_element(self.input_search_reagent)
        self.input_element(self.input_search_reagent, add_name)
        self.click_element(self.click_search_ensure)
        search = self.get_element_text(self.text_search)
        return search

    def alter_reagent(self, add_name):
        """
        :param add_name:
        :return: 继续新增
        """
        try:
            self.click_element(self.click_normal)
            self.input_element(self.input_add_name, add_name, num=10)
            self.click_element(self.click_save, num=0)
            sleep(5)
        except:
            return False
        else:
            return True

    def del_reagent(self):
        """
        :return: 删除耗材试剂
        """
        try:
            self.click_element(self.click_search_ensure)
            self.click_element(self.click_record, num=2)
            self.click_element(self.click_del)
            self.click_element(self.click_del_ensure)
        except:
            return False
        else:
            return True












