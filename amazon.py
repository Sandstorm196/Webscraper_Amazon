import uuid
from openpyxl import Workbook
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from pathlib import Path
from webdriver_manager.chrome import ChromeDriverManager

class amazon:
    '''This class scrapes the data from the Amazon website and saves it to a excel file.'''
    
    def __init__(self, url, links, phone_prices_list):
        '''Initializing webscaraper...'''
        print("Initializing webscaraper...")
        self.url = url
        self.links = links
        self.phone_prices_list = phone_prices_list

        # Chrome options
        opt = webdriver.ChromeOptions()
        opt.headless = True
        opt.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
        print("Options are initialized...")
        self.driver.get("https://www.amazon.co.uk/")
        self.driver.implicitly_wait(10)
        
    def accept_cookies(self):
        '''Accepting cookies...'''
        print("Accepting cookies...")
        
        xpath_accept_cookies = "//input[@type='submit' and @id='sp-cc-accept']"
        accept_button = self.driver.find_element(By.XPATH, xpath_accept_cookies)
        accept_button.click()
        time.sleep(2)
    
        # Scrape iPhone 13 data from Amazon website
    def search(self):
        '''Searching for the product in the Amazon website.'''
        
        print("Searching for the product...")
        
        search_term = "iPhone 13"
        xpath_search = "//input[@id='twotabsearchtextbox']"
        search_input = self.driver.find_element(By.XPATH, xpath_search)
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.RETURN)
        time.sleep(2)   
        
        print("Clicking on Apple...")
        xpath_click_apple = "//span[text()='Apple']"
        accept_button = self.driver.find_element(By.XPATH, xpath_click_apple)
        accept_button.click()
        time.sleep(2) 
        
        
      
    

    # def get_seller(self):
    #     try:
    #         return self.driver.find_element_by_id('bylineInfo').text
    #     except Exception as e:
    #         print(e)
    #         print(f"Can't get seller of a product - {self.driver.current_url}")
    #         return None    

    # def shorten_url(self, asin):
    #     return self.website + 'dp/' + asin
    
    # def get_single_product_info(self, asin):
    #     print(f"Product ID: {asin} - getting data...")
    #     product_short_url = self.shorten_url(asin)
    #     self.driver.get(f'{product_short_url}?language=en_GB')
    #     time.sleep(2)
    #     seller = self.get_seller()
    #     if seller:
    #         product_info = {
    #             'url': product_short_url,
    #             'seller': seller,
    #             'phone_prices_list': self.phone_prices_list,
    #         }
    #         return product_info
    #     return None
        

if __name__ == "__main__":  
    '''Initializing the class...'''
    
    amz = amazon("url", "phone_prices_list", "links")
    amz.accept_cookies()     
    amz.search()
    
    amz.driver.close()
    amz.driver.quit()
    
