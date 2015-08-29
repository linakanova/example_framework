
__author__ = 'lianakazanova'
from common import Common
import settings

from selenium.webdriver.common.by import By

class Cart(Common):
    def go_my_cart_page(self):
        self.env.driver.get('https://%s.connectedio.com/cart' % settings.site_env)

    def verify_product_in_cart(self, name):
        all_products_elements_in_cart = self.env.driver.find_elements(
            By.XPATH, "//*[@id='cartCheckout']/table[1]/tbody/tr/td[3]/a")
        for product_element in all_products_elements_in_cart:
            if product_element.text.lower() == name.lower():
                break
        else:
            assert False, 'Product %s was not found in my cart' % name