from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Member(BasePage):

    click_system = (By.CLASS_NAME, "el-menu-item")
    click_y = (By.CLASS_NAME, 'btn_yq')
    input_name = (By.CLASS_NAME, "el-input__inner")
    click_j = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div[1]/div[3]/table/tbody/tr[4]')
    click_save = (By.CLASS_NAME, "normal")
    click_x = (By.CLASS_NAME, 'el-table__row')
    click_t = (By.CLASS_NAME, 'btn_ty')
    click_q = (By.CLASS_NAME, 'el-button')
    click_qy = (By.CLASS_NAME, 'btn_qy')
    click_sc = (By.CLASS_NAME, 'btn_sc')
    click_ss = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/form/div/div/div[2]/div/div/button')
    click_z = (By.CLASS_NAME, 'el-icon-arrow-down')
    click_xs = (By.CLASS_NAME, 'el-checkbox__inner')

    def add_m(self, add_user, add_name):
        """
        :param add_user: 账户
        :param add_name: 姓名
        :return: 邀请成员
        """
        self.click_element(self.click_system, num=12)
        self.click_element(self.click_system, num=6)
        try:
            self.click_element(self.click_y)
            self.input_element(self.input_name, add_user, num=5)
            self.input_element(self.input_name, add_name, num=6)
            self.click_element(self.click_j)
            self.click_element(self.click_save)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_t(self):
        """
        :return: 停用账户
        """
        try:
            self.click_element(self.click_x, num=1)
            self.click_element(self.click_t)
            self.click_element(self.click_q, num=-1)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_q(self):
        """
        :return: 启用账户
        """
        try:
            self.click_element(self.click_qy)
            self.click_element(self.click_q, num=-1)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_s(self):
        """
        :return: 删除账户
        """
        try:
            self.click_element(self.click_x, num=0)
            self.click_element(self.click_sc)
            self.click_element(self.click_q, num=-1)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_ss(self, add_name):
        """
        :param add_name: 姓名
        :return: 搜索
        """
        try:
            self.input_element(self.input_name, add_name, num=2)
            self.click_element(self.click_ss)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_z(self):
        """
        :return: 自定义列显示
        """
        try:
            self.click_element(self.click_z, num=1)
            self.click_element(self.click_xs, num=-2)
            self.click_element(self.click_q, num=-1)
            sleep(2)
        except:
            return False
        else:
            return True








