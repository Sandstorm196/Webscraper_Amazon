import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ProductTestCase(unittest.TestCase):
    
    '''Initialize the scenario for the test'''
    
    def setUp(self):
        '''Initialize the scenario for the test'''
        
        self.webscraper = self.webscraper.jobsite()
        
    def test_scrape_data(self):
        '''Test the scrape data method.'''
        
        self.webscraper.scrape_data()
        
    def tearDown(self):
        
        '''Closes and terminates the driver...'''
        
        self.webscaraper.driver.close()
        self.webscaraper.driver.quit()
        
if __name__ == '__main__':
    
    unittest.main(argv=[''], verbosity=2, exit=False)