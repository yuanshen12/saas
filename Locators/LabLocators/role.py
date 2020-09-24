from selenium.webdriver.common.by import By
from Common.plugs.basepage import BasePage
import time


class Role(BasePage):

    click_role = (By.CLASS_NAME, "el-menu-item")
    click_add_role = (By.CLASS_NAME, "btn_xz1")
    input_role_name = (By.CLASS_NAME, "el-input__inner")
    click_save = (By.CLASS_NAME, "normal")
    click_role_text = (By.CLASS_NAME, "table-column-label")

    alter_ = (By.CLASS_NAME, "btn_sq")
    alter_choose = (By.CLASS_NAME, "big_font")
    alter_ensure = (By.CLASS_NAME, "normal")

    del_row = (By.CLASS_NAME, "el-table__row")
    del_row_name = (By.CLASS_NAME, "btn_sc")
    click_ensure = (By.CLASS_NAME, "el-button--small")

    def add_role(self, add_name):
        """
        :param add_name:
        :return: 新增角色
        """
        self.click_element(self.click_role, num=8)
        time.sleep(2)
        self.click_element(self.click_add_role)
        self.input_element(self.input_role_name, add_name, num=5)
        self.click_element(self.click_save, num=0)
        time.sleep(2)
        success_text = self.get_element_text(self.click_role_text, num=-3)
        return success_text

    def alter_role(self):
        """
        :return: 修改角色
        """
        self.click_element(self.alter_, num=-1)
        self.click_element(self.alter_choose, num=0)
        self.click_element(self.alter_choose, num=1)
        self.click_element(self.alter_ensure)
        time.sleep(2)
        success_text = self.get_element_text(self.click_role_text, num=-2)
        return success_text

    def del_role(self):
        """
        :return: 删除角色
        """
        try:
            self.click_element(self.del_row, num=-1)
            self.click_element(self.del_row_name)
            self.click_element(self.click_ensure, num=1)
        except:
            return False
        else:
            return True




