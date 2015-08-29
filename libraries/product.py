__author__ = 'lianakazanova'
from common import Common

from selenium.webdriver.common.by import By

class Product(Common):
    def add_current_product_to_cart(self):
        self.env.driver.find_element(By.CSS_SELECTOR, 'div.prod_detail a.addtocart').click()