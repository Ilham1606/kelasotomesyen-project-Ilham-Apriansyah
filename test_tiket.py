from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest


@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options) 
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://www.tiket.com/')
    yield driver
    time.sleep(3)
    driver.quit()

def test_kereta(setup):
    setup.find_element(By.CSS_SELECTOR, 'div.index_main___rT19 header.index_header__25ySr div.index_header_inner__ZgIbg div.index_content__k_CP2.index_desktop_only__ss43k:nth-child(5) div.SearchForm_verticalIcons__7QwNj div.VerticalIcons_listIcon__rGlIP div.VerticalIcons_wrapper__4jHIR ul.VerticalIcons_lastGrid__93rXJ li:nth-child(4) a:nth-child(1) > div.VerticalIcons_icon__M26iM').click()
    time.sleep(1)
    setup.find_element(By.CLASS_NAME, 'check').click()
    time.sleep(1)
    setup.find_element(By.CLASS_NAME, 'input-airport').send_keys('Jakarta')
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="formhome"]/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div/div/div[2]/ul/li[6]/div[2]/div[2]').click()
    time.sleep(1)
    setup.find_element(By.CSS_SELECTOR, 'div.left-side div.home-page div.content div.container div.flight-content div.home-train div.train-form.z-index-999:nth-child(1) div.form-style div.part-component.part-return:nth-child(3) div.content div.user-area div.station-list-area > input.input-airport').send_keys('Malang')
    time.sleep(1)
    setup.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[4]/div[2]/div[1]/span[1]').click()
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="formhome"]/div/div/div[1]/div[3]/div[4]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[7]/div').click()
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="formhome"]/div/div/div[1]/div[3]/div[5]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[6]/div').click()
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="formhome"]/div/div/div[1]/div[3]/div[6]/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/button/i').click()
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="formhome"]/div/div/div[1]/div[3]/div[6]/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button').click()
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="formhome"]/div/div/div[1]/div[3]/div[6]/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/button').click()
    time.sleep(1)
    setup.find_element(By.CSS_SELECTOR, '#formhome > div > div > div.train-form.z-index-999 > div.form-style > div.part-component.part-passenger > div.content > div > div > div.foot > button').click()
    time.sleep(1)
    setup.find_element(By.CSS_SELECTOR, '#formhome > div > div > div.train-form.z-index-999 > div.footer-part > button').click()

    result = setup.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[3]/div/div/div[2]/div[1]/div[1]/div').text
    assert result == 'Menampilkan semua kereta ke tujuanmu.'