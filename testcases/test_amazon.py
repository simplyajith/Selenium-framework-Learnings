import unittest
from selenium import webdriver
from framework.values import strings  # Make sure framework folder is present in system path(Environment variable)
from framework.pageobjects import homescreen,deals



class Test_amazon(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(strings.base_url)

    def test_home_screen_components(self):
        driver = self.driver
        home_screen = homescreen.Homescreen(driver)
        home_screen.validate_title_is_present()

    def test_deal_screen_components(self):
        driver = self.driver
        home_screen = homescreen.Homescreen(driver)
        home_screen.click_on_deal()
        deal_screen = deals.Dealscreen(driver)
        deal_screen.validate_title_is_present()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
