import uuid
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import os
import urllib
import socket
import ssl
import pandas as pd
import A_Const

class Amazon:
    
    def __init__(self):
        '''Initializing webscaraper...'''
        print("Initializing webscraper...")
        
        website = "https://www.amazon.co.uk/"
        opt = webdriver.ChromeOptions()
        opt.headless = True
        opt.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
        self.driver.get(website)
        self.driver.set_page_load_timeout(10)
        self.driver.implicitly_wait(10)
        # self.price_filter = f"&rh=p_36%3A{A_Const.FILTERS(max)}00-{A_Const.FILTERS(min)}00"
        
    def _accept_cookies(self):   
        '''Accepts cookies...'''     
        xpath_accept_cookies = "//input[@type='submit' and @id='sp-cc-accept']"
        accept_button = self.driver.find_element(By.XPATH, xpath_accept_cookies)
        accept_button.click()
        time.sleep(2)
        
    def _search(self):        
        '''Searching for the product in the Amazon website.'''
        print("Searching for the product...")
        
        search_term = "iPhone 13"
        xpath_search = "//input[@id='twotabsearchtextbox']"
        search_input = self.driver.find_element(By.XPATH, xpath_search)
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.RETURN)

        xpath_click_apple = "//span[text()='Apple']"
        accept_button = self.driver.find_element(By.XPATH, xpath_click_apple)
        accept_button.click()


    def get_price(self):
        
        print("Getting the price...")
   
        product_price = []
    
        prices = self.driver.find_elements(By.XPATH, "//span[contains(@class,'price-whole')]")
        #//span[@class='a-price']
        #//span[contains(@class,'price-whole')]
        for price in prices:
            print(price.text)


if __name__ == "__main__":  
    
    '''Main function...'''
    
    amz = Amazon()
    amz._accept_cookies()  
    amz._search()
    amz.get_price()

    amz.driver.close()
    amz.driver.quit()