import unittest
import Config
from unittest.case import _AssertRaisesContext
from Amazon import Amazon
import sys
import os
from selenium.common.exceptions import ElementNotInteractableException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# sys.path.append(os.path.pardir(os.path.pardir(__file__)))

sys.path.append("./Users/mansurcan/Documents/Ai_Core/Webscraper_Amazon/test_Amazon.py")

class Test(unittest.TestCase):
    '''
    Initialize the scenario for the public methods:
    - accept_cookies()
    - search()
    - click_on_brand()
    (Arrange, Act, Assert)
    '''
    def set_up(self):
        opt = webdriver.ChromeOptions()
        opt.headless = False
        opt.add_argument("--disable-notifications")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
        driver.get(Config.URL)
        driver.set_page_load_timeout(10)
        driver.implicitly_wait(10)
    
    def test_accept_cookies(self):
        '''Test the accept_cookies button whether it is clicked on.'''
        
        Amazon.accept_cookies("//input[@type='submit' and @id='sp-cc-accept']")
        with _AssertRaisesContext(ElementNotInteractableException):
            Amazon.accept_cookies("//input[@type='submit' and @id='sp-cc-accept']")
        
    # def test_search(self):
    #     '''Test the search term is on the website.'''
        
    #     expected_term = ['iPhone 13']
    #     actual_term = Amazon.search("//input[@id='twotabsearchtextbox']")
    #     self.assertEqual(expected_term, actual_term)
        
    # def test_click_on_brand(self):
        
    #     pass
        
        
    def tearDown(self):
        
        '''This is used to remove any of the variable set up from memory.'''
        self.driver.close()    
        
if __name__ == '__main__':
    '''Main method'''
    
    unittest.main()
    # amazon_scraper = Amazon()
    
    # suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
    # unittest.TextTestRunner().run(suite)
    
    
    # unittest.main(argv=[''], verbosity=2, exit=False)
    
     
  