from selenium import webdriver
from values import strings
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get(strings.base_url)
drop_down = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='nav-link-shopall']//span[@class='nav-line-2']")))
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(drop_down).perform()
driver.implicitly_wait(10)
time.sleep(6)
driver.quit()
