#https://seamaszhou.github.io/2019/09/29/Selenium-and-Jenkins/

import unittest
from selenium import webdriver

class TestCase(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Chrome("C:\\Users\\carolinem\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.driver = driver
        self.driver.get ("https://www.google.com")
        time.sleep(60)
        

   
    def tearDown(self):
        self.driver.close()
