from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://taniaksiazka.pl/')
auto_select = Select(driver.find_element_by)

time.sleep(5)
driver.quit()
