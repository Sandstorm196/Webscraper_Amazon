import unittest
import Config
from Amazon import Amazon

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
         
    
    def test_accept_cookies(self):
        '''Test the accept_cookies button whether it is clicked on.'''
        print("Test that the accept_cookies button is clicked on")
        
        self.assertEqual(self.amazon.accept_cookies, True)    
        
        
    def test_search(self):
        '''Test the search term is on the website.'''
        print("Test that search term is iPhone 13.")
        
        # self.assertEqual(Config.SEARCH_TERM, self.amazon.driver.)
        pass
        
    def test_click_on_brand(self):
        '''Test click on brand box when clicking on Apple brand.'''
        print("Test that click on brand box when clicking on Apple brand is working.")
        
        pass
        
        
    def tearDown(self):
        '''This is used to remove any of the variable set up from memory.'''
        print("Test tearDown called.")
        
        self.amazon.driver.close()   
        self.amazon.driver.quit() 
        
        
if __name__ == '__main__':
    '''Main method'''
    
    unittest.main()
    
     
  