from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://taniaksiazka.pl/')
search_field = driver.find_element('id', 'inputSearch')
search_field.clear()
search_field.send_keys('sapiens')
time.sleep(3)
search_button = driver.find_element('xpath', '//*[@id="search-form"]/fieldset/button')
search_button.submit()
driver.get_screenshot_as_file('screen.png')
time.sleep(3)
driver.quit()