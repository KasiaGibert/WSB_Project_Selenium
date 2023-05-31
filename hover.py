from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://taniaksiazka.pl/')
kategorie_element = driver.find_element("xpath", "//*[@id=\"main-menu\"]/li[1]/a")
webdriver.ActionChains(driver).move_to_element(kategorie_element).click(kategorie_element).perform()

time.sleep(5)
driver.quit()
