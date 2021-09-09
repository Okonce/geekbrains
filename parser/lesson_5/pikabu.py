from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

chrome_options = Options()
chrome_options.add_argument("start-maximized")

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)

driver.get("https://pikabu.ru/")

for i in range(5):
    articles = driver.find_elements_by_tag_name('article')
    actions = ActionChains(driver)
    actions.move_to_element(articles[-1]).key_down(Keys.ENTER)
    actions.perform()
    time.sleep(5)
