__author__ = 'lianakazanova'

import contact, faq, homepage, product, products, cart

class Main():
    def __init__(self, env):
        # Create POM objects:
        self.homepage = homepage.Homepage(env)
        # self.faq = faq.Faq(self)
        # self.contact = contact.Contact(self)
        self.product = product.Product(env)
        self.products = products.Products(env)
        self.cart = cart.Cart(env)