from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException


class Dealscreen:
    def __init__(self,driver):
        self.driver = driver
        self.timeout = 15
        self.title = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Filter Deals by Department')]")))


    def validate_title_is_present(self):
        try:
            assert self.title.is_displayed()
        except TimeoutException as ex:
            print "Element unclickable after {0} seconds".format(self.timeout)