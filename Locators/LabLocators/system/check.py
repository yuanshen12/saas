from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Check(BasePage):
    click_check = (By.CLASS_NAME, "el-menu-item")
    click_choose = (By.CLASS_NAME, "spanIcon")
    click_no = (By.CLASS_NAME, "el-radio__inner")
    save_home = (By.CLASS_NAME, "normal")

    def alter_check_yes(self):
        """
        :return: 审核流程，选择是
        """
        self.click_element(self.click_check, num=12)
        self.click_element(self.click_check, num=14)
        try:
            for x in range(7):
                sleep(1)
                self.click_element(self.click_choose, num=x)
                self.click_element(self.click_no, num=1)
                self.click_element(self.save_home)
        except:
            return False
        else:
            return True

    def alter_check_no(self):
        """
        :return: 审核流程，选择否
        """
        self.click_element(self.click_check, num=14)
        try:
            for x in range(7):
                sleep(1)
                self.click_element(self.click_choose, num=x)
                self.click_element(self.click_no, num=0)
                self.click_element(self.save_home)
        except:
            return False
        else:
            return True
