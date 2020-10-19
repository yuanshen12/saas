from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Member(BasePage):

    click_system = (By.CLASS_NAME, "el-menu-item")
    click_yq = (By.CLASS_NAME, 'btn_yq')
    input_ = (By.CLASS_NAME, 'el-input__inner')
    click_xz = (By.CLASS_NAME, 'el-table__row')
    save = (By.CLASS_NAME, 'normal')
    click_ss = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/form/div/div/div[2]/div/div/button')
    click_xq = (By.CLASS_NAME, 'btn_xq')
    click_sc = (By.CLASS_NAME, 'btn_sc')
    click_qr = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/button[2]')

    def get_a(self):
        """
        :return: 邀请成员
        """
        try:
            self.click_element(self.click_system, num=11)
            self.click_element(self.click_system, num=7)
            self.click_element(self.click_yq)
            self.click_element(self.save)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_b(self, add_user, add_name):
        """
        :param add_user: 账号
        :param add_name: 姓名
        :return: 邀请成员
        """
        try:
            self.input_element(self.input_, add_user, num=5)
            self.input_element(self.input_, add_name, num=6)
            self.click_element(self.click_xz, num=4)
            self.click_element(self.save)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_c(self, add_name):
        """
        :param add_name: 搜索名称
        :return: 搜索
        """
        try:
            self.input_element(self.input_, add_name, num=2)
            self.click_element(self.click_ss)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_d(self):
        """
        :return: 修改角色权限
        """
        try:
            self.click_element(self.click_xq)
            sleep(2)
            self.click_element(self.click_xz, num=3)
            self.click_element(self.save)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_f(self, add_name):
        """
        :return: 删除角色
        """
        try:
            self.get_element_rf()
            self.input_element(self.input_, add_name, num=2)
            self.click_element(self.click_ss)
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_sc)
            self.click_element(self.click_qr)
            sleep(2)
        except:
            return False
        else:
            return True

