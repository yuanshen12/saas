from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Purchase(BasePage):
    click_subscribe = (By.CLASS_NAME, "el-menu-item")
    click_add = (By.CLASS_NAME, "btn_xz1")
    input_name = (By.CLASS_NAME, "el-input__inner")

    click_name = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[3]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[2]/div')
    click_num = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[3]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[8]/div')
    click_sava = (By.CLASS_NAME, "normal")
    choose_ = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div[1]/div[3]/table/tbody/tr[1]')

    click_search = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/form/div/div/div[2]/div/div')
    text_search = (By.CLASS_NAME, 'table-column-label')

    click_even = (By.CLASS_NAME, "wl-gengduo")
    click_choose = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[1]')
    click_c = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/div/div[1]/div[1]/div[3]/table/tbody/tr[2]')
    click_check = (By.CLASS_NAME, "btn_sh")

    check_no = (By.CLASS_NAME, "el-radio__inner")
    click_place = (By.CLASS_NAME, 'btn_xd')

    click_w = (By.CLASS_NAME, "wl-icon-container1")
    click_g = (By.CLASS_NAME, 'el-select-dropdown__item')
    click_n = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[2]')
    click_s = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[7]')

    def add_pc(self, m_name, s_name, n_num=2):
        """
        :param m_name: 采购商品名称
        :param s_name: 采购商家名称
        :param n_num: 采购数量
        :return: 采购流程
        """
        try:
            self.click_element(self.click_subscribe, num=8)
            self.click_element(self.click_subscribe, num=3)
            for i in range(3):
                self.click_element(self.click_add)
                self.input_element(self.input_name, s_name, num=15)
                self.click_element(self.click_name)
                self.input_element(self.input_name, m_name, num=20)
                self.click_element(self.click_num)
                self.input_element(self.input_name, n_num, num=20)
                if i == 0:
                    self.click_element(self.click_sava, num=1)
                elif i == 1:
                    self.click_element(self.click_sava, num=2)
                else:
                    self.click_element(self.click_sava, num=0)
                    self.click_element(self.choose_)
                    self.click_element(self.click_sava, num=3)
                    self.click_element(self.click_sava, num=1)
                sleep(2)
                i += 1
        except:
            return False
        else:
            return True

    def search_pc(self, add_name):
        """
        :param add_name: 搜索商家名称
        :return: 搜索功能
        """
        self.input_element(self.input_name, add_name, num=3)
        self.click_element(self.click_search)
        sleep(2)
        search = self.get_element_text(self.text_search, num=4)
        return search

    def place_pc(self):
        """
        :return: 下单流程
        """
        even = self.get_element_text(self.click_even)
        if even == "更多":
            self.click_element(self.click_even)
        try:
            self.click_element(self.click_choose)
            self.click_element(self.click_place, num=0)
        except:
            return False
        else:
            return True

    def check_pc(self, choose=None):
        """
        :param choose: 审核通过判断
        :return: 审核流程
        """
        even = self.get_element_text(self.click_even)
        if even == "更多":
            self.click_element(self.click_even)
        try:
            if choose is None:
                self.click_element(self.click_choose)
                self.click_element(self.click_check, num=0)
            else:
                self.click_element(self.click_c)
                self.click_element(self.click_check, num=0)
                self.click_element(self.check_no, num=1)
            self.click_element(self.click_sava, num=0)
            sleep(2)
        except:
            return False
        else:
            return True

    def enquiry_pc(self, add_name, add_num):
        """
        :param add_name: 商品名称
        :param add_num: 商品数量
        :return: 询价流程
        """
        try:
            self.click_element(self.click_place, num=1)
            self.click_element(self.click_sava, num=1)
            self.click_element(self.click_w)
            self.input_element(self.input_name, add_name, num=15)
            self.click_element(self.click_n)
            self.input_element(self.input_name, add_name, num=15)
            self.click_element(self.click_s)
            self.input_element(self.input_name, add_num, num=15)
            self.click_element(self.click_sava, num=3)
            sleep(2)
        except:
            return False
        else:
            return True


