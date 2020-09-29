from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Subscribe(BasePage):
    click_subscribe = (By.CLASS_NAME, "el-menu-item")
    click_add = (By.CLASS_NAME, "btn_sg")
    click_name = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[2]/div')
    input_name = (By.CLASS_NAME, "el-input__inner")
    click_t = (By.CLASS_NAME, "operation_cell")
    click_sum = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[5]/div')
    click_sava = (By.CLASS_NAME, "normal")

    click_search = (By.CLASS_NAME, "el-button--mini")
    search_text = (By.CLASS_NAME, "table-column-label")

    click_choose = (By.CLASS_NAME, "el-table__row")
    click_check = (By.CLASS_NAME, "btn_sh")
    click_no = (By.CLASS_NAME, "el-radio")

    click_del = (By.CLASS_NAME, "btn_sc")
    ensure_del = (By.CLASS_NAME, "el-button--small")

    def add_su(self, add_name, add_sum):
        """
        :param add_sum: 申购数量
        :param add_name: 申购商品名称
        :return: 添加申购订单
        """
        try:
            self.click_element(self.click_subscribe, num=0)
            self.click_element(self.click_subscribe, num=8)
            self.click_element(self.click_subscribe, num=2)
            for i in range(2):
                self.click_element(self.click_add)
                self.click_element(self.click_name)
                self.input_element(self.input_name, add_name, num=8)
                self.click_element(self.click_t, num=-2)
                self.click_element(self.click_sum)
                self.input_element(self.input_name, add_sum, num=8)
                self.click_element(self.click_sava)
        except:
            return False
        else:
            return True

    def search_su(self, search_name):
        """
        :param search_name: 商品名称
        :return: 搜索商品
        """
        sleep(2)
        self.input_element(self.input_name, search_name, num=3)
        self.click_element(self.click_search, num=6)
        text = self.get_element_text(self.search_text)
        return text

    def check_su(self, choose=None, num=0):
        """
        :param num: 选择审核记录
        :param choose: 选择是否同意审核
        :return: 审核流程
        """
        try:
            self.click_element(self.click_choose, num=num)
            self.click_element(self.click_check, num=0)
            if choose is not None:
                self.click_element(self.click_no, num=1)
            self.click_element(self.click_sava)
        except:
            return False
        else:
            return True

    def del_su(self, num=1):
        """
        :param num: 选择记录
        :return: 删除流程
        """
        try:
            self.click_element(self.click_choose, num=num)
            self.click_element(self.click_del)
            self.click_element(self.ensure_del, num=1)
            sleep(2)
        except:
            return False
        else:
            return True

