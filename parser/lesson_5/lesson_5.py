from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

chrome_options = Options()
chrome_options.add_argument("--window-size=750,1080")

driver = webdriver.Chrome(executable_path='/Users/assimarakhimbekova/PycharmProjects/geekbrains/parser/lesson_5/chromedriver',
                          options=chrome_options)

driver.get("https://gb.ru/login")

login = driver.find_element_by_id('user_email')
login.send_keys('study.ai_172@mail.ru')

passw = driver.find_element_by_id('user_password')
passw.send_keys('Password172')

passw.send_keys(Keys.ENTER)


menu = driver.find_element_by_xpath("//span[text()='РјРµРЅСЋ']")
menu.click()

but = driver.find_element_by_xpath("//button[@data-test-id='user_dropdown_menu']")
but.click()

profile = driver.find_element_by_xpath("//li/a[contains(@href,'/users/')]")
profile_url = profile.get_attribute('href')
driver.get(profile_url)

edit_profile = driver.find_element_by_class_name("text-sm")
driver.get(edit_profile.get_attribute('href'))

gender = driver.find_element_by_name('user[gender]')
select = Select(gender)

select.select_by_value('female')

gender.submit()

print()



# driver.close()