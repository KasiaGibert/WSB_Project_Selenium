from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://www.taniaksiazka.pl")

print(driver.find_element("id", "logo").size.get("height"))
print(driver.find_element("id", "logo").get_attribute("naturalHeight"))


time.sleep(1)
driver.quit()