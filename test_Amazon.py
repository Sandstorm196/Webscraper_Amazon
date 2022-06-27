import unittest
import Config
from unittest.case import _AssertRaisesContext
from Amazon import Amazon
import sys
import os
import time
from selenium.common.exceptions import ElementNotInteractableException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

sys.path.append(os.path.pardir(os.path.pardir(__file__)))

# sys.path.append("./Users/mansurcan/Documents/Ai_Core/Webscraper_Amazon/test_Amazon.py")

class Test(unittest.TestCase):
    '''
    Initialize the scenario for the public methods:
    - accept_cookies()
    - search()
    - click_on_brand()
    (Arrange, Act, Assert)
    '''
    
    def setUp(self):
        '''Setting up the environment'''
        
        opt = webdriver.ChromeOptions()
        opt.headless = False
        opt.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
        self.driver.get(Config.URL)
        self.driver.set_page_load_timeout(10)
        self.driver.implicitly_wait(10)
    
    def test_website(self):
        '''Test that website is Amazon.'''
        
        URL = "https://www.amazon.co.uk/"
        self.driver.get(URL)        
        self.assertEqual(URL,Config.URL)
         
    
    def test_accept_cookies(self):
        '''Test the accept_cookies button whether it is clicked on.'''
        
        Amazon.accept_cookies("//input[@type='submit' and @id='sp-cc-accept']")
        with self.assertRaises(ElementNotInteractableException):
            Amazon.accept_cookies("//input[@type='submit' and @id='sp-cc-accept']")
        
    def test_search(self):
        '''Test the search term is on the website.'''
        
        expected_term = ['iPhone 13']
        actual_term = Amazon.search("//input[@id='twotabsearchtextbox']")
        self.assertEqual(expected_term, actual_term)
        
    def test_click_on_brand(self):
        '''Test click on brand box when clicking on Apple brand.'''
        
        pass
        
        
    def tearDown(self):
        '''This is used to remove any of the variable set up from memory.'''
        
        self.driver.close()   
        self.driver.quit() 
        
if __name__ == '__main__':
    '''Main method'''
    
    unittest.main()
    
     
  