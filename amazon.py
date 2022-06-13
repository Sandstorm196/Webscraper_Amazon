# Necessary web-scaraper packages
import uuid
from jmespath import search
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
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
import os
import csv
import json
from webdriver_manager.chrome import ChromeDriverManager

class amazon:
    '''This class scrapes the data from the Amazon website and saves it to a excel file.'''
    
    def __init__(self, url, links, website, object_uuid, phone_names_list, phone_prices_list):
        '''Initializing webscaraper...'''
        print("Initializing webscaraper...")
        self.website = "https://www.amazon.co.uk/"
        self.url = url
        self.links = links
        self.object_uuid = object_uuid
        self.phone_names_list = phone_names_list
        self.phone_prices_list = phone_prices_list

        # Chrome options
        opt = webdriver.ChromeOptions()
        opt.headless = True
        opt.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
        print("Options are initialized...")
        self.driver.get(website)
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
        time.sleep(2) # The page is loading slowly
        
        print("Clicking on Apple...")
        xpath_click_apple = "//span[text()='Apple']"
        accept_button = self.driver.find_element(By.XPATH, xpath_click_apple)
        accept_button.click()
        time.sleep(2) # The page is loading slowly
        
        self.driver.get(f'self.current_url')
        print(f'The current URL is : {self.driver.current_url}' )
        time.sleep(2) # The page is loading slowly
        results_list = self.driver.find_elements_by_class_name('s-result-list')
        self.links = []
        
        try:
            results = results_list[0].find_elements_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span')
            self.links = [link.get_attribute('href') for link in results]
            return self.links
        except Exception as e:
            print("Couldn't find the product...")
            print(e)
        
        # UUID 
        object_uuid = []
        for i in range(26):
            uuidFour = str(uuid.uuid4())
            object_uuid.append(uuidFour)
        print("uuid of version four", uuid)

        # Phone SKU
        xpath_phone_names = "//span[contains(@class,'a-size-medium a-color-base a-text-normal')]"
        phone_names = self.driver.find_elements(By.XPATH, xpath_phone_names)
        print("Found " + str(len(phone_names)) + " results")
        
        phone_names_list = []
        for names in phone_names:
            phone_names_list.append(names.text)
        print(phone_names_list)
        
        # Stars
        xpath_stars = "//div[@class='a-row a-size-small']/span[1]"
        stars = self.driver.find_elements(By.XPATH, xpath_stars).text
        print("Found " + str(len(stars)) + " results")
        
        stars_list = []
        for star in stars:
            stars_list.append(star.text)
        print(stars_list)
        
        # Reviews
        xpath_reviews = "//div[@class='a-row a-size-small']/span[2]"
        reviews = self.driver.find_elements(By.XPATH, xpath_reviews).text
        print("Found " + str(len(reviews)) + " results")
        
        reviews_list = []
        for review in reviews:
            reviews_list.append(review.text)
        print(reviews_list)
        
    def get_products_info(self, links):
        '''It gets products information...'''
        asins = self.get_asins(links)
        products = []
        for asin in asins:
            product = self.get_single_product_info(asin)
            if product:
                products.append(product)
        return products

    def get_asins(self, links):
        '''It gets product asins...'''
        return [self.get_asin(link) for link in links]
    
    def get_seller(self):
        try:
            return self.driver.find_element_by_id('bylineInfo').text
        except Exception as e:
            print(e)
            print(f"Can't get seller of a product - {self.driver.current_url}")
            return None    
    
    def get_asin(product_link):
        return product_link[product_link.find('/dp/') + 4:product_link.find('/ref')]

    def shorten_url(self, asin):
        return self.website + 'dp/' + asin
    
    def get_single_product_info(self, asin):
        print(f"Product ID: {asin} - getting data...")
        product_short_url = self.shorten_url(asin)
        self.driver.get(f'{product_short_url}?language=en_GB')
        time.sleep(2)
        seller = self.get_seller()
        if seller:
            product_info = {
                'uuid': self.object_uuid,
                'asin': asin,
                'url': product_short_url,
                'seller': seller,
                'phone_names_list': self.phone_names_list,
                'phone_prices_list': self.phone_prices_list,
            }
            return product_info
        return None
        

if __name__ == "__main__":  
    '''Initializing the class...'''
    
    amz = amazon("url","website","phone_names_list","phone_prices_list","object_uuid","links")
    amz.accept_cookies()     
    amz.search()
    amz.get_products_info(amz.links)
    amz.get_asins(amz.links)
    amz.get_seller()
    amz.shorten_url(amz.links)
    amz.get_single_product_info(amz.links)
    
    amz.driver.close()
    amz.driver.quit()
    
