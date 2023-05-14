from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://taniaksiazka.pl/')
driver.find_element(By.ID, 'inputSearch')