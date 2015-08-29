__author__ = 'lianakazanova'

from selenium import webdriver

import settings

class Env():
    def __init__(self):
        # Create webdriver object:
        if settings.browser == 'Firefox':
            self.driver = webdriver.Firefox()
        if settings.browser == 'Chrome':
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def quit(self):
        self.driver.quit()