from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from pages.base import BasePage


class ProductsPage(BasePage):

    dress_selector = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a')
    add_to_cart_selector = (By.XPATH, "//a[@class='button ajax_add_to_cart_button btn btn-default']")
    checkout_button_selector = (By.XPATH, "//a[@title='Proceed to checkout']")

    def add_element_to_cart(self):
        dress = self.driver.find_element(*self.dress_selector)
        hover = ActionChains(self.driver).move_to_element(dress)
        hover.perform()
        self.driver.find_element(*self.add_to_cart_selector).click()


    def proceed_to_checkout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.checkout_button_selector)).click()










