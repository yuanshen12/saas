from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Supplier(BasePage):
    click_supplier = (By.CLASS_NAME, "el-menu-item")
    click_add_supplier = (By.CLASS_NAME, "btn_xz1")
    input_add_name = (By.CLASS_NAME, "el-input__inner")
    click_save = (By.CLASS_NAME, "normal")
    text_supplier = (By.CLASS_NAME, "table-column-label")

    input_search_reagent = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/form/div/div/div[2]/div/input')
    click_search_ensure = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/form/div/div/div[2]/div/div')
    text_search = (By.CLASS_NAME, "table-column-label")

    click_normal = (By.CLASS_NAME, 'btn_xq')
    click_name = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[3]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[2]')

    click_record = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[1]')
    click_del = (By.CLASS_NAME, "btn_sc")
    click_del_ensure = (By.CLASS_NAME, 'el-button--small')

    def add_supplier(self, add_name):
        """
        :param add_name:
        :return: 新增供应商
        """
        self.click_element(self.click_supplier, num=10)
        sleep(1)
        self.click_element(self.click_add_supplier)
        self.input_element(self.input_add_name, add_name, num=5)
        self.click_element(self.click_save, num=0)
        add_text = self.get_element_text(self.text_supplier, num=1)
        return add_text

    def search_supplier(self, search_name):
        """
        :param search_name:
        :return: 搜索供应商
        """
        self.click_element(self.input_search_reagent)
        self.input_element(self.input_search_reagent, search_name)
        self.click_element(self.click_search_ensure)
        sleep(1)
        search = self.get_element_text(self.text_search, num=1)
        return search

    def alter_supplier(self, alter_name):
        """
        :param alter_name:
        :return: 编辑供应商
        """
        self.click_element(self.click_normal)
        self.click_element(self.click_name)
        self.input_element(self.input_add_name, alter_name, num=22)
        self.click_element(self.click_save, num=0)
        add_text = self.get_element_text(self.text_supplier, num=2)
        return add_text

    def del_supplier(self):
        """
        :return: 删除供应商
        """
        try:
            self.click_element(self.click_search_ensure)
            self.click_element(self.click_record)
            self.click_element(self.click_del)
            self.click_element(self.click_del_ensure, num=1)
        except:
            return False
        else:
            return True
