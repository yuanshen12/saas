from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Commodity(BasePage):

    click_system = (By.CLASS_NAME, "el-menu-item")
    click_ad = (By.CLASS_NAME, 'btn_xz1')
    save = (By.CLASS_NAME, 'normal')
    click_mz = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[2]/div')
    input_ = (By.CLASS_NAME, 'el-input__inner')
    click_sl = (By.CLASS_NAME, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div[2]/form[2]/div/div[1]/div[3]/table/tbody/tr/td[10]/div')



    def get_a(self):
        """
        :return: 申购流程
        """
        self.click_element(self.click_system, num=1)
        self.click_element(self.click_system, num=2)
        try:
            self.click_element(self.click_ad)
            self.click_element(self.save, num=0)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_b(self, add_name, add_num):
        self.click_element(self.click_mz)
        self.input_element(self.input_, add_name, num=8)
        self.click_element(self.click_sl)
        self.input_element(self.input_, add_num, num=8)
        self.click_element(self.save, num=0)

