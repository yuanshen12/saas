from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Role(BasePage):

    click_system = (By.CLASS_NAME, "el-menu-item")
    click_ad = (By.CLASS_NAME, 'btn_xz1')
    input_ = (By.CLASS_NAME, 'el-input__inner')
    save = (By.CLASS_NAME, 'normal')
    click_qx = (By.CLASS_NAME, 'btn_sq')
    click_sz = (By.CLASS_NAME, 'one_item_top')
    click_ss = (By.XPATH, '//*[@id="app"]/div/div[5]/section/div/form/div/div/div[2]/div/div/button')
    click_xz = (By.CLASS_NAME, 'no-event')
    click_sc = (By.CLASS_NAME, 'btn_sc')
    click_qr = (By.CLASS_NAME, 'el-button--small')

    def get_a(self, add_name):
        """
        :param add_name: 岗位名称
        :return: 新增岗位
        """
        self.click_element(self.click_system, num=11)
        self.click_element(self.click_system, num=9)
        try:
            self.click_element(self.click_ad)
            sleep(1)
            self.input_element(self.input_, add_name, num=5)
            self.click_element(self.save)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_b(self, num=0):
        """
        :return: 设置权限
        """
        try:
            self.click_element(self.click_qx, num=-1)
            sleep(1)
            if num == 0:
                self.click_element(self.click_sz, num=0)
            elif num == 1:
                self.click_element(self.click_sz, num=1)
            elif num == 2:
                self.click_element(self.click_sz, num=2)
            self.click_element(self.save)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_c(self, add_name):
        """
        :param add_name: 商品名称
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
        :return: 删除角色
        """
        try:
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_sc)
            self.click_element(self.click_qr, num=-1)
            sleep(2)
        except:
            return False
        else:
            return True

