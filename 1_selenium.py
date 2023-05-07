from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://gotujemy.pl')
time.sleep(3)
driver.quit()