from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


import time

chrome_options = Options()
chrome_options.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)

driver.get("https://lenta.com/catalog/myaso-ptica-kolbasa/")

driver.find_element_by_class_name('close-control').click()

time.sleep(2)


page = 0
while page < 3:
    wait = WebDriverWait(driver, 10)
    button_wait = wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, 'catalog-grid-container__pagination-button')
    ))
    # button = driver.find_element_by_class_name('catalog-grid-container__pagination-button')
    button_wait.click()
    page += 1


meat = driver.find_elements_by_class_name('sku-card-small-container')

for m in meat:
    print(m.find_element_by_class_name('sku-card-small__title').text)
