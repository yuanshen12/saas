import pytest
from PIL import Image, ImageEnhance
from selenium import webdriver


@pytest.fixture(scope='session')
def login():
    chromedriver = '../software/chromedriver.exe'
    driver = webdriver.Chrome(chromedriver)
    driver.get('http://192.168.0.156:8901/')
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.find_element_by_class_name("el-input__inner").click()
    driver.find_elements_by_class_name("el-select-dropdown__item")[0].click()
    driver.find_elements_by_class_name("test_login-btn")[0].click()
    driver.save_screenshot('../img/img_01.png')
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