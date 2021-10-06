#https://seamaszhou.github.io/2019/09/29/Selenium-and-Jenkins/

import unittest
import base
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class GoogleTest(base.TestCase):
  
    def test_google_search(self):
        driver = base.driver
        try:
            elem = driver.find_element_by_name("q")
            elem.send_keys("python")
            elem.send_keys(Keys.ENTER)
            print ('Everything working okay') 
        except NoSuchElementException:            
            print ('No results found.') 

if __name__ == '__main__':
    unittest.main()