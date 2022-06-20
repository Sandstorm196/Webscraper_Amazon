import unittest
from Amazon2 import scrape_data
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ProductTestCase(unittest.TestCase):
    
    '''Initialize the scenario for the test'''
        
    def test_scrape_data(self):
        '''Test the scrape data method.'''
        
        self.assertAlmostEqual(len(self.webscaraper.scrape_data()), 25)
        
    def tearDown(self):
        
        '''Closes and terminates the driver...'''
        print("Closing the driver...")
        
        self.webscaraper.driver.close()
        self.webscaraper.driver.quit()
        
if __name__ == '__main__':
    '''Main method'''
    
    unittest.main(argv=[''], verbosity=2, exit=False)