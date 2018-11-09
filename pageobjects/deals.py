from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Dealscreen:
    def __init__(self,driver):
        self.driver = driver
        self.title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Filter Deals by Department')]")))


    def validate_title_is_present(self):
        assert self.title.is_displayed()