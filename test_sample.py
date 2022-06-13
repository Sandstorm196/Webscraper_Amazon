import unittest
import sys

sys.path.append('/Users/mansurcan/Documents/Ai_Core/Webscraper/jobsite')

class ProductTestCase(unittest.TestCase):
    
    '''Initialize the scenario for the test'''
    
    def setUp(self):
        '''Initialize the scenario for the test'''
        
        self.webscraper = webscraper.jobsite()
        
    def test_transform_name(self):
        expected_value = 'SHOES'
        actual_value = self.product.transform_name_for_sku()
        self.assertEqual(expected_value, actual_value)
        
    def tearDown(self):
        
        '''Closes and terminates the driver...'''
        
        self.webscaraper.driver.close()
        self.webscaraper.driver.quit()
        
if __name__ == '__main__':
    
    unittest.main(argv=[''], verbosity=2, exit=False)