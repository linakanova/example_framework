__author__ = 'lianakazanova'

import unittest

from libraries.env import Env
from libraries.main import Main

import libraries.settings as settings

class Main_test_suite(unittest.TestCase):
    def setUp(self):
        self.env = Env() #  self.env it is a object of class Env()
        self.main = Main(self.env)

    def tearDown(self):
        self.env.quit()

    def test_invalid_login(self):
        self.main.homepage.go_home_page()
        self.main.homepage.login(settings.existing_user_data['user1']['login'],
                            settings.existing_user_data['user1']['password'] + '#@RGSF$G')

    def test_verify_new_product_in_cart_by_name(self):
        self.main.products.go_products_page()
        self.main.products.go_product('LT1000 2G/3G/4G USB M2M Modem')
        self.main.product.add_current_product_to_cart()
        self.main.cart.go_my_cart_page()
        self.main.cart.verify_product_in_cart('LT1000 2G/3G/4G USB M2M Modem')

    def test_verify_new_product_in_cart_by_number(self):
        # Better solution for cart check
        self.main.products.go_products_page()
        product_name = self.main.products.go_product_by_number(1)
        self.main.product.add_current_product_to_cart()
        self.main.cart.go_my_cart_page()
        self.main.cart.verify_product_in_cart(product_name)


if __name__ == '__main__':
    unittest.main()