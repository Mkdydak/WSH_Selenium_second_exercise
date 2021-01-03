from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from pages.base import BasePage


class CartSummary(BasePage):
    total_product_selector = (By.ID, 'total_product')
    total_shipping_selector = (By.ID, 'total_shipping')

    def price_smaller_than_50(self):
        price = self.driver.find_element(*self.total_product_selector).text
        assert float(price.strip('$')) < 50

    def total_shipping_2_dollars(self):
        shipping = self.driver.find_element(*self.total_shipping_selector).text
        assert float(shipping.strip('$')) == 2

