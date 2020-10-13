from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep

class Role(BasePage):

    click_role = (By.CLASS_NAME, "el-menu-item")
    click_add_role = (By.CLASS_NAME, "btn_xz1")
    input_role_name = (By.CLASS_NAME, "el-input__inner")
    click_save = (By.CLASS_NAME, "normal")
    click_role_text = (By.CLASS_NAME, "table-column-label")

    alter_ = (By.CLASS_NAME, "btn_sq")
    alter_choose = (By.CLASS_NAME, "big_font")
    alter_ensure = (By.CLASS_NAME, "normal")

    del_row_name = (By.CLASS_NAME, "btn_sc")
    click_ensure = (By.CLASS_NAME, "el-button--small")
    click_ss = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/form/div/div/div[2]/div/div/button')
    click_sc = (By.CLASS_NAME, 'no-event')

    def add_role(self, add_name):
        """
        :param add_name:
        :return: 新增角色
        """
        self.click_element(self.click_role, num=12)
        self.click_element(self.click_role, num=8)
        sleep(2)
        self.click_element(self.click_add_role)
        self.input_element(self.input_role_name, add_name, num=5)
        self.click_element(self.click_save, num=0)
        sleep(2)
        success_text = self.get_element_text(self.click_role_text, num=-3)
        return success_text

    def alter_role(self):
        """
        :return: 修改角色
        """
        self.click_element(self.alter_, num=-1)
        self.click_element(self.alter_choose, num=0)
        self.click_element(self.alter_ensure)
        sleep(2)
        success_text = self.get_element_text(self.click_role_text, num=-2)
        return success_text

    def add_t(self, add_name):
        """
        :param add_name:
        :return: 新增角色2
        """
        try:
            self.click_element(self.click_add_role)
            self.input_element(self.input_role_name, add_name, num=5)
            self.click_element(self.click_save, num=0)
            sleep(2)
        except:
            return False
        else:
            return True

    def alter_t(self):
        """
        :return: 修改权限
        """
        try:
            self.click_element(self.alter_, num=-1)
            self.click_element(self.alter_choose, num=1)
            self.click_element(self.alter_ensure)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_ss(self, add_name):
        """
        :param add_name: 搜索名称
        :return: 搜索
        """
        try:
            self.input_element(self.input_role_name, add_name, num=2)
            self.click_element(self.click_ss)
            sleep(2)
        except:
            return False
        else:
            return True

    def del_role(self):
        """
        :return: 删除角色
        """
        try:
            self.click_element(self.click_sc, num=0)
            self.click_element(self.del_row_name)
            self.click_element(self.click_ensure, num=1)
            sleep(2)
        except:
            return False
        else:
            return True




