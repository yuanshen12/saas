import pytest
from PIL import Image, ImageEnhance
from selenium.webdriver.common.by import By
import os
driver = None
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

login_loc = (By.CLASS_NAME, "el-input__inner")


@pytest.fixture(scope='class')
def start_module(project_session_start):
    global driver
    driver = project_session_start
    driver.get('http://192.168.0.156:8901/')
    driver.maximize_window()
    driver.implicitly_wait(20)
    print(login_loc)
    # driver.find_element(login_loc).click()
    driver.find_element_by_class_name("el-input__inner").click()
    driver.find_elements_by_class_name("el-select-dropdown__item")[0].click()
    driver.find_elements_by_class_name("login-btn")[0].click()
    save_path = PATH('../img/img_01.png')
    driver.save_screenshot(save_path)
    left_img = driver.find_element_by_class_name('el-input-group__append').location
    left = left_img['x']
    top = left_img['y']
    image = driver.find_element_by_class_name('el-input-group__append')
    width = image.size['width']
    height = image.size['height']
    right = left + width
    down = top + height
    img_save = Image.open('../img/img_01.png')
    img = img_save.crop((left, top, right, down))
    img.save('../img/img_02.png')
    img = img.convert('RGBA')
    img = img.convert('L')
    img = ImageEnhance.Contrast(img)
    img = img.enhance(2.0)
    img.save('../img/img_03.png')
    yield driver
    driver.quit()
