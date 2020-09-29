from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Home(BasePage):
    click_home = (By.CLASS_NAME, "el-menu-item")
    click_add_home = (By.CLASS_NAME, "btn_tjfj")
    input_name = (By.CLASS_NAME, "el-input__inner")
    click_type = (By.CLASS_NAME, "width1")
    choose_type = (By.CLASS_NAME, "hover")
    save_home = (By.CLASS_NAME, "normal")

    input_search_reagent = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/form/div/div/div[2]/div/input')
    click_search_ensure = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/form/div/div/div[2]/div/div')
    text_search = (By.CLASS_NAME, "table-column-label")

    click_alter = (By.CLASS_NAME, "btn_xq")
    text_alter = (By.CLASS_NAME, "table-column-label")

    def add_home(self, home_name):
        """
        :param home_name:
        :return: 添加房间
        """
        self.click_element(self.click_home, num=11)
        try:
            self.click_element(self.click_add_home)
            self.input_element(self.input_name, home_name, num=5)
            self.click_element(self.click_type)
            self.click_element(self.choose_type)
            self.click_element(self.save_home)
        except:
            return False
        else:
            return True

    def search_home(self, search_name):
        """
        :param search_name:
        :return: 搜索房间
        """
        sleep(1)
        self.click_element(self.click_home, num=11)
        self.click_element(self.input_search_reagent)
        self.input_element(self.input_search_reagent, search_name)
        self.click_element(self.click_search_ensure)
        sleep(1)
        search = self.get_element_text(self.text_search, num=0)
        return search

    def alter_home(self, alter_name):
        """
        :param alter_name: 门牌号
        :return: 修改房间
        """
        self.click_element(self.click_alter)
        self.input_element(self.input_name, alter_name, keys_control=1, num=8)
        self.click_element(self.save_home)
        self.click_element(self.click_search_ensure)
        text = self.get_element_text(self.text_alter, num=1)
        return text




