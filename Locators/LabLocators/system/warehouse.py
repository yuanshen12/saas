from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Warehouse(BasePage):
    click_home = (By.CLASS_NAME, "el-menu-item")
    click_add_wh = (By.CLASS_NAME, "success")
    input_name = (By.CLASS_NAME, "el-input__inner")
    save_home = (By.CLASS_NAME, "normal")

    input_search_reagent = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/form/div/div/div[2]/div/input')
    click_search_ensure = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/form/div/div/div[2]/div/div')
    text_search = (By.CLASS_NAME, "table-column-label")

    click_alter = (By.CLASS_NAME, "btn_xq")

    choose_wh = (By.CLASS_NAME, "no-event")
    click_del_wh = (By.CLASS_NAME, "btn_sc")
    click_ensure = (By.CLASS_NAME, "el-button--small")

    def add_warehouse(self, add_name):
        """
        :param add_name: 仓库名称
        :return: 新增仓库
        """
        self.click_element(self.click_home, num=12)
        self.click_element(self.click_home, num=12)
        try:
            self.click_element(self.click_add_wh, num=0)
            self.input_element(self.input_name, add_name, num=5)
            self.click_element(self.save_home)
        except:
            return False
        else:
            return True

    def search_wh(self, search_name):
        """
        :param search_name: 商品名
        :return: 搜索
        """
        self.click_element(self.input_search_reagent)
        self.input_element(self.input_search_reagent, search_name)
        self.click_element(self.click_search_ensure)
        sleep(1)
        search = self.get_element_text(self.text_search, num=0)
        return search

    def alter_wh(self, alter_name):
        """
        :param alter_name: 楼层位置
        :return: 修改楼层位置
        """
        self.click_element(self.click_alter)
        self.input_element(self.input_name, alter_name, num=7)
        self.click_element(self.save_home)
        self.click_element(self.click_search_ensure)
        alter = self.get_element_text(self.text_search, num=1)
        return alter

    def del_wh(self):
        """
        :return: 删除仓库
        """
        try:
            self.click_element(self.choose_wh)
            self.click_element(self.click_del_wh)
            self.click_element(self.click_ensure, num=1)
        except:
            return False
        else:
            return True

