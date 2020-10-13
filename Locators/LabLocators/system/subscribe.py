from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Subscribe(BasePage):

    click_system = (By.CLASS_NAME, "el-menu-item")

    click_subscribe = (By.CLASS_NAME, "el-menu-item")
    click_message = (By.CLASS_NAME, "el-button--text")
    click_choose = (By.CLASS_NAME, "el-radio__inner")
    click_save = (By.CLASS_NAME, "normal")

    click_add = (By.CLASS_NAME, "spanIcon")
    input_name = (By.CLASS_NAME, "el-input__inner")
    success_name = (By.CLASS_NAME, "line-height")

    click_ensure = (By.CLASS_NAME, "el-button--small")

    click_x = (By.CLASS_NAME, 'el-radio__inner')
    click_y = (By.CLASS_NAME, 'el-checkbox__inner')

    def get_subscribe(self, choose):
        """
        :param choose: fend_start开启资金，fend_stop关闭资金
        :return:
        """
        self.click_element(self.click_system, num=12)
        self.click_element(self.click_subscribe, num=7)
        self.click_element(self.click_message, num=0)
        try:
            if choose == "fend_start":
                self.click_element(self.click_choose, num=0)
                self.click_element(self.click_save, num=1)
            elif choose == "fend_stop":
                self.click_element(self.click_choose, num=1)
                self.click_element(self.click_save, num=1)
        except:
            return False
        else:
            return True

    def get_gr(self, add_num):
        """
        :param add_num: 个人资金
        :return: 修改个人资金
        """
        sleep(2)
        try:
            self.click_element(self.click_message, num=0)
            self.input_element(self.input_name, add_num, num=12)
            self.click_element(self.click_save, num=1)
        except:
            return False
        else:
            return True

    def get_sq(self):
        """
        :return: 是否需要申请
        """
        try:
            self.click_element(self.click_message, num=0)
            self.click_element(self.click_x, num=2)
            self.click_element(self.click_x, num=4)
            self.click_element(self.click_save, num=1)
        except:
            return False
        else:
            return True

    def get_y(self, num):
        """
        :param num:
        :return: 选择业务
        """
        try:
            self.click_element(self.click_message, num=0)
            if num == 2:
                self.click_element(self.click_y, num=2)
            elif num == 1:
                self.click_element(self.click_y, num=2)
                self.click_element(self.click_y, num=1)
            elif num == 0:
                self.click_element(self.click_y, num=1)
            self.click_element(self.click_save, num=1)
        except:
            return False
        else:
            return True

    def get_add_sub(self, add_name):
        """
        :param add_name:
        :return: 增加项目组
        """
        self.click_element(self.click_add, num=0)
        self.input_element(self.input_name, add_name, keys_control=0, num=2)
        self.click_element(self.click_save)
        sleep(1)
        add_text = self.get_element_text(self.success_name, num=4)
        return add_text

    def get_details(self, add_name):
        """
        :param add_name:
        :return: 修改项目组
        """
        self.click_element(self.click_add, num=4)
        self.input_element(self.input_name, add_name, keys_control=1, num=2)
        self.click_element(self.click_save)
        sleep(1)
        success_text = self.get_element_text(self.success_name, num=4)
        return success_text

    def get_del(self):
        """
        :return: 删除项目组
        """
        try:
            self.click_element(self.click_add, num=5)
            self.click_element(self.click_ensure, num=1)
        except:
            return False
        else:
            sleep(2)
            return True