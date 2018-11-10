from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Homescreen:
    def __init__(self,driver):
        self.driver = driver
        self.title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='nav-sprite nav-logo-base']")))
        self.deal = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//a[contains(text(),\'Deals\')]')))
        #self.popup_ship = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text()')))
        self.drop_down = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.nav-line-2')))
        self.books = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//span[@class='nav-text'][contains(text(),'Books')]")))



    def validate_title_is_present(self):
        assert self.title.is_displayed()

    # def popup_ship_is_present(self):
    #     if self.popup_ship.is_present():
    #         self.popup_ship.click()
    #     else:
    #         print "No popup present"

    def click_on_deal(self):
        self.deal.click()

        #assert self.deal.is_displayed()
    def validate_dropdown_in_home_screen_is_present(self):
        assert self.drop_down.is_displayed()

    def validate_books_in_drop_down(self):
        self.driver.implicitly_wait(10)
        hover = ActionChains(self.driver).move_to_element(self.drop_down)
        hover.perform()
        assert self.books.is_displayed()









