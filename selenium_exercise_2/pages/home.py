from selenium.webdriver.common.by import By

from pages.base import BasePage

class HomePage(BasePage):

    search_field_selector = (By.ID, 'search_query_top')
    submit_search_button_selector = (By.NAME, 'submit_search')


    def search_product(self, product_name):
        self.driver.find_element(*self.search_field_selector).clear()
        self.driver.find_element(*self.search_field_selector).send_keys(product_name)
        self.driver.find_element(*self.submit_search_button_selector).click()

