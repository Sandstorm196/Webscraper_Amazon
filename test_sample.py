import unittest
import sys

sys.path.append('/Users/mansurcan/Documents/Ai_Core/Webscraper/jobsite')

class ProductTestCase(unittest.TestCase):
    
    '''Initialize the scenario for the test'''
    
    def setUp(self):
        '''Initialize the scenario for the test'''
        
        self.webscraper = self.webscraper.jobsite()
        
    def test_scrape_data(self):
        '''Test the scrape data method.'''
        
        self.webscraper.scrape_data()
        self.assertEqual(len(self.webscraper.job_results), 10)
        
    def tearDown(self):
        
        '''Closes and terminates the driver...'''
        
        self.webscaraper.driver.close()
        self.webscaraper.driver.quit()
        
if __name__ == '__main__':
    
    unittest.main(argv=[''], verbosity=2, exit=False)