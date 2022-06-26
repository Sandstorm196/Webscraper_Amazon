import unittest
from unittest.case import _AssertRaisesContext
import Amazon
import sys
import os
from selenium.common.exceptions import ElementNotInteractableException

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestDemo(unittest.TestCase):
    
    '''
    Initialize the scenario for the public methods:
    - accept_cookies()
    - search()
    - click_on_brand()
    '''
    
    def test_accept_cookies():
        '''Test the accept_cookies button whether it is clicked on.'''
        
        Amazon.accept_cookies("//input[@type='submit' and @id='sp-cc-accept']")
        with _AssertRaisesContext(ElementNotInteractableException):
            Amazon.accept_cookies("//input[@type='submit' and @id='sp-cc-accept']")
        
    # def test_search(self):
    #     '''Test the search term is on the website.'''
        
    #     expected_term = ['iPhone 13']
    #     actual_term = self.search("//input[@id='twotabsearchtextbox']")
    #     self.assertEqual(expected_term, actual_term)
        
    # def test_click_on_brand(self):
        
    #     pass
        
        
    def tearDown(self):
        
        '''This is used to remove any of the variable set up from memory.'''
        del self.Amazon
    
        
    
    
if __name__ == '__main__':
    '''Main method'''
    
    unittest.main(argv=[''], verbosity=2, exit=False)