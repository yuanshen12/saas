from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from time import sleep


class Commodity(BasePage):

    click_system = (By.CLASS_NAME, "el-menu-item")
    click_ad = (By.CLASS_NAME, 'btn_xz1')
    input_ = (By.CLASS_NAME, 'el-input__inner')
    click_lxx = (By.CLASS_NAME, 'el-cascader__label')
    click_lx = (By.CLASS_NAME, 'el-cascader-menu__item')
    save = (By.CLASS_NAME, 'normal')
    click_xq = (By.CLASS_NAME, 'btn_xq')
    click_xz = (By.CLASS_NAME, 'el-table__row')
    click_ty = (By.CLASS_NAME, 'btn_sz')
    click_qr = (By.CLASS_NAME, 'el-button--small')
    click_zd = (By.CLASS_NAME, 'sjjbsz')
    click_xd = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div/form[2]/div/div[1]/div[3]/table/tbody/tr/td[3]/div')
    click_sc = (By.CLASS_NAME, 'btn_sc')
    click_tc = (By.CLASS_NAME, 'wl-title-buttons')
    click_fl = (By.CLASS_NAME, 'btn_flbq')
    click_bq = (By.CLASS_NAME, 'el-tabs__item')
    click_dk = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/form/div/div[2]/div/div/div[2]/div[4]/div/form[2]/div/div[1]/div[3]/table/tbody/tr/td[2]/div')
    click_ss = (By.CLASS_NAME, 'el-icon-search')

    def get_a(self):
        """
        :return: 新增商品
        """
        self.click_element(self.click_system, num=11)
        self.click_element(self.click_system, num=10)
        try:
            self.click_element(self.click_ad)
            self.click_element(self.save, num=0)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_b(self, add_name):
        """
        :param add_name: 商品名称
        :return: 新增商品
        """
        try:
            self.input_element(self.input_, add_name, num=6)
            self.click_element(self.click_lxx)
            self.click_element(self.click_lx, num=1)
            self.click_element(self.save, num=0)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_c(self, add_num):
        """
        :param add_num: 采购单价
        :return:修改商品
        """
        try:
            self.click_element(self.click_xq, num=0)
            self.input_element(self.input_, add_num, keys_control=1, num=15)
            self.click_element(self.save, num=0)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_d(self, add_num):
        """
        :param add_num: 售价
        :return: 修改商品
        """
        try:
            self.click_element(self.click_xq, num=0)
            self.input_element(self.input_, add_num, keys_control=1, num=16)
            self.click_element(self.save, num=0)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_f(self, add_nums, add_num):
        """
        :param add_nums: 库存上限
        :param add_num: 库存下限
        :return: 修改商品
        """
        try:
            self.click_element(self.click_xq, num=0)
            self.input_element(self.input_, add_nums, keys_control=1, num=18)
            self.input_element(self.input_, add_num, keys_control=1, num=20)
            self.click_element(self.save, num=0)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_g(self, add_num):
        """
        :param add_num: 销售单价
        :return: 修改通用设置
        """
        try:
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_ty)
            self.input_element(self.input_, add_num, keys_control=1, num=7)
            self.click_element(self.save, num=0)
            self.click_element(self.click_qr, num=1)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_h(self, add_name):
        """
        :param add_name: 级别名称
        :return: 自定义售价级别
        """
        try:
            self.click_element(self.click_zd)
            self.click_element(self.save, num=0)
            sleep(1)
            self.click_element(self.click_xd)
            self.input_element(self.input_, add_name, num=6)
            self.click_element(self.save, num=1)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_j(self):
        """
        :return: 删除自定义售价级别
        """
        try:
            self.click_element(self.click_zd)
            self.click_element(self.click_sc, num=1)
            self.click_element(self.click_qr, num=1)
            self.click_element(self.click_tc)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_k(self, add_bq):
        """
        :param add_bq: 标签名字
        :return: 设置标签
        """
        try:
            self.click_element(self.click_fl)
            self.click_element(self.click_bq, num=1)
            self.click_element(self.click_dk)
            self.input_element(self.input_, add_bq, num=6)
            self.click_element(self.click_tc)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_s(self):
        """
        :return: 设置分类和标签
        """
        try:
            self.click_element(self.click_fl)
            self.click_element(self.click_bq, num=1)
            self.click_element(self.click_sc, num=-1)
            self.click_element(self.click_tc)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_z(self, add_name):
        """
        :param add_name: 搜索名称
        :return: 搜索商品
        """
        try:
            self.input_element(self.input_, add_name, num=3)
            self.click_element(self.click_ss, locate="element1", num=1)
            sleep(2)
        except:
            return False
        else:
            return True

    def get_w(self):
        """
        :return: 删除
        """
        try:
            self.click_element(self.click_xz, num=0)
            self.click_element(self.click_sc)
            self.click_element(self.click_qr, num=1)
        except:
            return False
        else:
            return True







