from selenium import webdriver
import time

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://taniaksiazka.pl/')
log_in = driver.find_element('xpath', '//*[@id="user-box"]/div[1]/p/a/strong')
log_in.click()
name_field = driver.find_element('id', 'registerFirstName')
name_field.send_keys('Katarzyna')
last_name_field = driver.find_element('id', 'registerLastName')
last_name_field.send_keys('Gibert')
phone_number_field = driver.find_element('id', 'registerPhone')
phone_number_field.send_keys('723922689')
email_field = driver.find_element('id', 'registerEmail')
email_field.send_keys('katarzyna.gibert@gmail.com')
password_field = driver.find_element('id', 'registerPassword')
password_field.send_keys('kasiagibert')
password1_field = driver.find_element('id', 'registerPassword1')
password1_field.send_keys('kasiagibert')
checkbox = driver.find_element('id', 'registerAgree')
checkbox.click
create_account = driver.find_element('id', 'CreateAccountSubmit')
create_account.submit()
time.sleep(5)


'''
search_field = driver.find_element('id', 'inputSearch')
search_field.clear()
search_field.send_keys('sapiens')
time.sleep(3)
search_button = driver.find_element('xpath', '//*[@id="search-form"]/fieldset/button')
search_button.submit()
'''


driver.get_screenshot_as_file('screen.png')
time.sleep(3)
driver.quit()
