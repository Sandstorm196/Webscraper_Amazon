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
    
    def __init__(self):
        print("Initializing webscaraper...")
        website = "https://www.amazon.co.uk/"
        
        # Chrome options
        opt = webdriver.ChromeOptions()
        opt.headless = True
        opt.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
        print("Options are initialized...")
        self.driver.get(website)
        self.driver.implicitly_wait(10)
        
    def accept_cookies(self):
        print("Accepting cookies...")
        
        xpath_accept_cookies = "//input[@type='submit' and @id='sp-cc-accept']"
        accept_button = self.driver.find_element(By.XPATH, xpath_accept_cookies)
        accept_button.click()
        time.sleep(2)
    
        # Scrape iPhone 13 data from Amazon website
    def search(self):
        
        print("Searching for the product...")
        
        search_term = "iPhone 13"
        xpath_search = "//input[@id='twotabsearchtextbox']"
        search_input = self.driver.find_element(By.XPATH, xpath_search)
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.RETURN)
        time.sleep(5)
        
        print("Clicking on Apple...")
        xpath_click_apple = "//span[text()='Apple']"
        accept_button = self.driver.find_element(By.XPATH, xpath_click_apple)
        accept_button.click()
        time.sleep(2)
        
        # UUID 
        object_uuid = []
        for i in range(18):
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
                
        # Phone prices
        xpath_phone_prices = "//span[contains(@class,'price-whole')]"
        phone_prices = self.driver.find_elements(By.XPATH, xpath_phone_prices)
        print("Found " + str(len(phone_prices)) + " results")
        
        phone_prices_list = []
        for price in phone_prices:
            phone_prices_list.append(price.text)
        print(phone_prices_list)
        
        # Images
        images_iphone = []
        # elements = self.driver.find_elements_by_xpath("//img[@class='s-image']")
        elements = self.driver.find_elements_by_xpath("a-section aok-relative s-image-fixed-height")

        for i in elements:
            image = i.get_attribute("src")
            images_iphone.append(image)
        
        for img in images_iphone:
            file_name = img.split("/")[-1]
            print(f"This is the file name: {file_name}")
        
        r = requests.get(img, stream=True)
        
        if r.status_code == 200:
            with open(file_name, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
        else:
            print("Image could not be downloaded")
        
        # Beautiful Soup
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        results = soup.find_all("div", {"class": "s-result-item"})
        
        # Rating
        # xpath_rating = "//i[@class='a-icon a-icon-star-small a-star-small-5 aok-align-bottom' and //span[@class='a-icon-alt']]"
        # rating = self.driver.find_elements(By.XPATH, xpath_rating)
        # print("Found " + str(len(rating)) + " results")
        
        # rating_list = []
        # for ratings in rating:
        #     rating_list.append(ratings.text)
        # print(rating_list)
        
        # Final list file, save in an excel document
        final_list = zip(object_uuid, phone_names_list, phone_prices_list, images_iphone)    
        
        # keys = ['uuid', 'phone_name', 'phone_price', 'operating_system']
        
        # dictionary = dict(zip(keys, final_list))
        # print(dictionary)
         
        wb = Workbook()
        wb['Sheet'].title = 'iPhone13_Raw_Data'
        sheet1 = wb.active
        sheet1.append(['UUID','SKU', 'Phone_Price', 'Image'])
        
        for data in list(final_list):
            sheet1.append(data)
        
        wb.save("iPhone13_Raw_Data.xlsx")
        print("Raw data saved...")

if __name__ == "__main__":  
    amz = amazon()
    amz.accept_cookies()     
    amz.search()

    amz.driver.close()
    amz.driver.quit()
    
