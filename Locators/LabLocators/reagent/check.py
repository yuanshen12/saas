from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Check(BasePage):

    click_subscribe = (By.CLASS_NAME, "el-menu-item")
    click_add = (By.CLASS_NAME, 'btn_xz1')
    click_sk = (By.CLASS_NAME, 'wl-icon-container1')
    click_sava = (By.CLASS_NAME, "normal")
    click_xz = (By.CLASS_NAME, 'el-table__row')
    click_tj = (By.CLASS_NAME, 'btn_tj')
    click_sh = (By.CLASS_NAME, 'btn_sh')
    click_cl = (By.CLASS_NAME, 'btn_cl')

    def add_ck(self):
        """
        :return: 盘点新增流程
        """
        self.click_element(self.click_subscribe, num=8)
        self.click_element(self.click_subscribe, num=9)
        try:
            self.click_element(self.click_add)
            self.click_element(self.click_sk)
            self.click_element(self.click_sava)
        except:
            return False
        else:
            return True

    def add_tj(self):
        """
        :return: 提交
        """
        try:
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_tj)
        except:
            return False
        else:
            return True

    def add_sh(self):
        """
        :return: 审核
        """
        try:
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_sh)
            self.click_element(self.click_sava)
        except:
            return False
        else:
            return True

    def add_cl(self):
        """
        :return: 盈亏处理
        """
        try:
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_cl)
        except:
            return False
        else:
            return True
