from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Check(BasePage):

    click_system = (By.CLASS_NAME, "el-menu-item")
    click_xz = (By.CLASS_NAME, 'el-table__row')
    click_ys = (By.CLASS_NAME, 'btn_rk')
    click_sl = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[12]/div')
    save = (By.CLASS_NAME, 'normal')
    input_ = (By.CLASS_NAME, 'el-input__inner')
    click_xz1 = (By.CLASS_NAME, 'no-event')


    def get_a(self):
        """
        :return: 验收入库
        """
        self.click_element(self.click_system, num=0)
        self.click_element(self.click_system, num=7)
        try:
            sleep(2)
            self.click_element(self.click_system, num=3)
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_ys)
            self.click_element(self.save)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_b(self, add_num):
        """
        :param add_num: 入库数量
        :return: 验收入库
        """
        try:
            self.click_element(self.click_xz1, num=-2)
            self.click_element(self.click_sl)
            self.input_element(self.input_, add_num, num=9)
            self.click_element(self.save)
            sleep(2)
        except:
            return False
        else:
            return True

