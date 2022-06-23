from dataclasses import dataclass
import uuid
from openpyxl import Workbook
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import os
import urllib
import pandas as pd
import Config
import time

@dataclass
class Data:
    
    opt = webdriver.ChromeOptions()
    opt.headless = False
    opt.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
    driver.get(Config.URL)
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)
    
    num_page = 5
    
    price_list = []
    sku_list = []
    asin_list = []
    reviews_list = []
    image_link_list = []
    product_link_list = []


class Amazon(Data):
    
    def __init__(self):
        '''Initializing webscaraper...'''
        print("Initializing webscraper...")
        
                
    def accept_cookies(self):   
        '''Accepts cookies...'''     
        print("Accepting cookies...")
        
        time.sleep(2)
        accept_button = self.driver.find_element(By.XPATH, Config.XPATH_COOKIES)
        accept_button.click()
        self.driver.implicitly_wait(10)
        

    def search(self):        
        '''Searching for the product in the Amazon website.'''
        print("Searching for the product...")
        
        search_input = self.driver.find_element(By.XPATH, Config.XPATH_SEARCH_BOX)
        search_input.send_keys(Config.SEARCH_TERM)
        search_input.send_keys(Keys.RETURN)
        

    def click_on_brand(self):
        accept_button = self.driver.find_element(By.XPATH, Config.XPATH_APPLE_BRAND)
        accept_button.click()
        
        
    def _create_images_folder(self):
        '''It creates the images folder.'''
        print('Creating images folder...')
        
        self.image_path = os.getcwd()
        self.image_path = os.path.join(self.image_path, 'iPhone_13_images')
        
        if not os.path.exists(self.image_path):
            os.mkdir(self.image_path)
            print(self.image_path)
            
        
    def _download_images(self):
        '''Downloads images from the Amazon website.'''
        print("Downloading images...")

        page = 1
        count = 1
        
        try:
            img_element = self.driver.find_element(by=By.XPATH, value=Config.XPATH_IMAGES).get_attribute('src')
            print(len(img_element))

            for i in img_element: 
                urllib.request.urlretrieve(i, os.path.join(self.image_path, f'page_{page}' + '_image_' + str(count) + '.jpg'))
                count += 1
                page += 1
                
        except Exception as e:
            print('Could not get the image:', e)
                        
    
    def _get_price(self):
        '''It gets the price of a product from the website.'''
        print('Get the price of a product from the website')
            
        price_element = self.driver.find_elements(by=By.XPATH, value=Config.XPATH_PRICES)
        print(len(price_element))
        
        for price in price_element:  
            print(len(price.text))  
            
            if price.text == None:
                price.text == 'Empty'
                self.price_list.append(price.text)
            else:
                self.price_list.append(price.text)
            print(self.price_list) 
                

    def _get_sku(self):
        '''It gets the sku from the website.'''
        print('Get the sku from the website...')
            
        sku_element = self.driver.find_elements(by=By.XPATH, value=Config.XPATH_SKU)
        print(len(sku_element))
        
        for sku in sku_element:  
            print(len(sku.text))  
            
            if sku.text == None:
                sku.text == 'Empty'
                self.sku_list.append(sku.text)
            else:
                self.sku_list.append(sku.text)
            print(self.sku_list)
            
        
    def _get_asin(self):
        '''It gets the asin of the product from the website.'''
        print('Get the asin of the product from the website')
                    
        asin_element = self.driver.find_elements(by=By.XPATH, value=Config.XPATH_ASIN)
        print(len(asin_element))
        
        for asin in asin_element:  
            print(len(asin.get_attribute('data-asin')))  
            
            if asin.text == None:
                asin.text == 'Empty'
                self.asin_list.append(asin.get_attribute('data-asin'))
            else:
                self.asin_list.append(asin.get_attribute('data-asin'))
            print(self.asin_list)
         
    
    def _get_reviews(self):
        '''It gets the number of reviews.'''
        print('Get the number of reviews...')
                    
        reviews_element = self.driver.find_elements(by=By.XPATH, value=Config.XPATH_REVIEWS)
        print(len(reviews_element))
        
        for reviews in reviews_element:  
            print(len(reviews.text))  
            
            if reviews == None:
                reviews == 'Empty'
                self.reviews_list.append(reviews)
            else:
                self.reviews_list.append(reviews.text)
            print(self.reviews_list)
            

    def _get_image_link(self):
        '''It gets image links.'''
        print('Get image links...')
       
        image_link_element = self.driver.find_elements(by=By.XPATH, value=Config.XPATH_IMAGE_LINK)
        print(len(image_link_element))
        
        for image_link in image_link_element:  
            print(len(image_link.get_attribute('src')))  
            
            if image_link.text == None:
                image_link.text == 'Empty'
                self.image_link_list.append(image_link.get_attribute('src'))
            else:
                self.image_link_list.append(image_link.get_attribute('src'))
            print(self.image_link_list)
     
     
    def _get_product_link(self):
        '''It gets the product links.'''
        print('Get product links...')
                            
        product_link_element = self.driver.find_elements(by=By.XPATH, value=Config.XPATH_PRODUCT_LINK)
        print(len(product_link_element))
        
        for product_link in product_link_element:  
            print(len(product_link.get_attribute('href')))  
            
            if product_link.text == None:
                product_link.text == 'Empty'
                self.product_link_list.append(product_link.get_attribute('href'))
            else:
                self.product_link_list.append(product_link.get_attribute('href'))
            print(self.product_link_list)
            
                
    def _save_data(self):
        '''It saves the data.'''
        print("It is saving the data in the json and excel file.")
                                
        final_list = zip(self.price_list, 
                         self.sku_list, 
                         self.asin_list, 
                         self.reviews_list, 
                         self.product_link_list, 
                         self.image_link_list)       
        
        df_data = pd.DataFrame(final_list, columns=['price',
                                                    'sku', 
                                                    'asin', 
                                                    'reviews', 
                                                    'product_link', 
                                                    'image_link'])
                        
        df_data.to_excel('iPhone_13_Data.xlsx', index=False)
        df_data.to_json('iPhone_13_Data.json', orient='records')
                        
        print(df_data)                 
        
        
    def scrape_data(self):
        '''It scrapes all the data...'''
        print('Scraping all the data...')
        
        self._create_images_folder()
        
        for page in range(self.num_page):
            
            print(f'Page: {page + 1}')

            self._download_images()
            self._get_price()
            self._get_sku()
            self._get_asin()
            self._get_reviews()
            self._get_image_link()
            self._get_product_link()
            self._save_data()
        
            time.sleep(3)
            next = self.driver.find_element(by=By.XPATH, value=Config.XPATH_NEXT_PAGE)
            next.click()
                
                
if __name__ == "__main__":  
    
    '''Main function...'''
    
    amz = Amazon()
    amz.accept_cookies()  
    amz.search()
    amz.click_on_brand()
    amz.scrape_data()

    amz.driver.close()
    amz.driver.quit()
    
    print("Done!")