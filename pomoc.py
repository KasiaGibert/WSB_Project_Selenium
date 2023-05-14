from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://taniaksiazka.pl/')

try:
earch_field = driver.find_element('id', 'inputSearch')
except:
    raise