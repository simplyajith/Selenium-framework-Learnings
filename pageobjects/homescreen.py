from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Homescreen:
    def __init__(self,driver):
        self.driver = driver
        self.title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='nav-sprite nav-logo-base']")))
        self.deal = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//a[contains(text(),\'Deals\')]')))


    def validate_title_is_present(self):
        assert self.title.is_displayed()

    def click_on_deal(self):
        self.deal.click()
        #assert self.deal.is_displayed()


