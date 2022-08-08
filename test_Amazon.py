import unittest
import Config
from Amazon import Amazon
from selenium.common.exceptions import ElementNotInteractableException
from unittest.mock import mock_open, patch, Mock
import webbrowser


class Test(unittest.TestCase):
    '''
    Initialize the scenario for the public methods:
    - accept_cookies()
    - search()
    - click_on_brand()
    (Arrange, Act, Assert)
    '''
    def setUp(self):
        '''Setting the environment.'''
        print('Setting the environment by creating Amazon object.')
        
        self.amazon = Amazon()
        
        
    def test_init(self):
        '''Test that website is Amazon.'''
        print("Test that website is Amazon.")
        
        self.assertEqual(self.amazon.driver.current_url, Config.URL)
         
    @patch('Amazon.Amazon.accept_cookies')
    def test_accept_cookies(
        self, 
        mock_cookies: Mock,
        ):
        
        '''Test the accept_cookies button whether it is clicked on.'''
        print("Test that the accept_cookies button is clicked on")
        
        self.amazon.driver.get(Config.URL)
        self.amazon.accept_cookies()
        mock_cookies.assert_called_once()
        
        cookies_call_count = mock_cookies.call_count
        self.assertEqual(cookies_call_count, 1)
    
    @patch('selenium.webdriver.remote.webelement.WebElement.send_keys')
    def test_search(self, mock_send_keys: Mock):
        '''Test the search term is on the website.'''
        print("Test that search term is iPhone 13.")
        
        self.amazon.driver.get(Config.URL)
        self.amazon.accept_cookies()
        self.amazon.search()
        mock_send_keys.assert_called()
        
    @patch('selenium.webdriver.remote.webelement.WebElement.click')
    def test_click_on_brand(self, mock_click: Mock):
        '''Test click on brand box when clicking on Apple brand.'''
        print("Test that click on brand box when clicking on Apple brand is working.")
        
        self.amazon.driver.get(Config.URL)
        self.amazon.accept_cookies()
        self.amazon.search()
        self.amazon.click_on_brand()
        
        mock_click.assert_called()
        
        
    def tearDown(self):
        '''This is used to remove any of the variable set up from memory.'''
        print("Test tearDown called.")
        
        self.amazon.driver.quit() 
        del self.amazon
        
        
if __name__ == '__main__':
    '''Main method'''
    
    unittest.main()
    
     
  