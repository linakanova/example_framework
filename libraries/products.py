__author__ = 'lianakazanova'
from common import Common
import settings

from selenium.webdriver.common.by import By

class Products(Common):
    def go_products_page(self):
        self.env.driver.get('https://%s.connectedio.com/products' % settings.site_env)

    def go_product(self, name):
        self.env.driver.find_element(By.PARTIAL_LINK_TEXT, name).click()

    def go_product_by_number(self, number):
        product_xpath = '//ul[@class="list_product"]/li[{product_number}]//h3/a'.format(product_number=str(number))
        product_element = self.env.driver.find_element(By.XPATH, product_xpath)
        product_element.click()
        return product_element.text
