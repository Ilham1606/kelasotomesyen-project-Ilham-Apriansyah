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
    driver.get('https://bromotenggersemeru.org/')
    yield driver
    time.sleep(3)
    driver.quit()

def test_booking(setup):
    # <-- Action Chain -->
    navbar = setup.find_element(By. XPATH, '//*[@id="menu-main-menu"]/li[10]/a')
    bookSemeru = setup.find_element(By. XPATH, '//*[@id="menu-main-menu"]/li[10]/ul/li[1]/a')

    actions = ActionChains(setup)
    actions.move_to_element(navbar)
    actions.move_to_element(bookSemeru)
    actions.click(bookSemeru)
    actions.perform()

    homePage = setup.find_element(By.ID, 'main-menu')
    assert homePage
    # <-- End of Action Chain --> 

    setup.find_element(By.CSS_SELECTOR, 'div.call-to-action-sec:nth-child(3) div.container div.row div.col-md-4.col-sm-3 div.call-to-action-text > a.btn').click()
    setup.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[16]/a').click()
    setup.find_element(By.XPATH, '//*[@id="cnt-checklist"]/div/div[2]/div/div/ul/li[1]/label/input').click() #checkbox1
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="cnt-checklist"]/div/div[2]/div/div/ul/li[2]/label/input').click() #checkbox2
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="cnt-checklist"]/div/div[2]/div/div/ul/li[3]/label/input').click() #checkbox3
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="cnt-checklist"]/div/div[2]/div/div/ul/li[4]/label/input').click() #checkbox4
    time.sleep(1)
    setup.find_element(By.XPATH, '//*[@id="cnt-checklist"]/div/div[2]/div/div/ul/li[5]/label/input').click() #checkbox5
    time.sleep(2)
    setup.find_element(By.XPATH, '//*[@id="cnt-checklist"]/div/div[4]/input').click()

    formPendaftaran = setup.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/h2').text
    assert formPendaftaran