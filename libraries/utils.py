

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element_visible(driver, locator_type, locator, timeout=30,\
                             message='Element with name {locator} not nound'):
    '''
    this function for wait element visible on the page
    '''
    try:
        return WebDriverWait(driver, timeout).until(

               EC.presence_of_element_located((locator_type, locator)))
    except:
        message += ' after ' + str(timeout) + ' secs. '
        assert False, message.format(locator=locator)
