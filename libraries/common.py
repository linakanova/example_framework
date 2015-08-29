__author__ = 'lianakazanova'
import time
import locators
from  utils import wait_for_element_visible
from selenium.webdriver.common.by import By


class Common():
    def __init__(self, env):
        self.env = env

    def go_home_page(self):
        self.env.driver.get('https://www.connectedio.com/')

    def go_about_us(self):
        pass

    def go_all_product(self):
        pass

    def login(self, email, password):
        login_text_field = self.env.driver.find_element_by_link_text(locators.sign_in_button)
        login_text_field.click()
        self.env.driver.find_element_by_name(locators.user_name_login_field).send_keys(email)
        self.env.driver.find_element_by_name(locators.user_name_password_field).send_keys(password)
        self.env.driver.find_element_by_xpath(locators.login_submit_button).click()
        error_message =wait_for_element_visible(self.env.driver, By.CLASS_NAME, 'log_error')
        assert 'Invalid Email or Password' in error_message.text
