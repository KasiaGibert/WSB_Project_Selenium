from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://taniaksiazka.pl/')
log_in = driver.find_element('xpath', '//*[@id="user-box"]/div[1]/p/a/strong')
log_in.click()
email_field = driver.find_element('id', 'loginEmail')
email_field.send_keys('katarzyna.gibert@gmail.com')
password_field = driver.find_element('id', 'loginPassword')
password_field.send_keys('kasiagibert')
log_in_button = driver.find_element('xpath', '//*[@id="LoginPage"]/form[1]/p/button')
log_in_button.submit()

time.sleep(5)
driver.quit()
