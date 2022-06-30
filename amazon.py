from dataclasses import dataclass, field
from unittest import result
from dataclasses_json import dataclass_json
import uuid
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
import os
import urllib
import pandas as pd
import Config
import time

@dataclass_json
@dataclass()
class Data:    
    price_list : list = field(default_factory=list) 
    sku_list : list = field(default_factory=list) 
    asin_list : list = field(default_factory=list) 
    reviews_list : list = field(default_factory=list) 
    image_link_list : list = field(default_factory=list) 
    product_link_list : list = field(default_factory=list) 
    uuidFour : list = field(default_factory=list) 

class Amazon:
    
    def __init__(self):
        '''Initializing webscaraper...'''
        print("Initializing webscraper...")
        
        opt = webdriver.ChromeOptions()
        opt.headless = True
        opt.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
        self.driver.get(Config.URL)
        self.driver.set_page_load_timeout(10)
        self.driver.implicitly_wait(10)
        self.num_page = 1
        self.product_data_container = Data()
                
    def accept_cookies(self):   
        '''Accepts cookies...'''     
        print("Accepting cookies...")
        
        time.sleep(2)
        try: 
            accept_button = self.driver.find_element(By.XPATH, Config.XPATH_COOKIES)
            accept_button.click()
            time.sleep(2)
        except  NoSuchElementException as e:
            print("TimeoutException, cookies button has not been clicked:", e)
            

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
        '''Downloads images from the Amazon website with the given number of the page.'''
        print("Downloading images...")

        count = 1
        time.sleep(7)
        
        try:
            img_element = self.driver.find_elements(by=By.XPATH, value=Config.XPATH_IMAGES)
            print(len(img_element))

            src = [i.get_attribute('src') for i in img_element]
            print(len(src))
            
            for i in src: 
                urllib.request.urlretrieve(i, os.path.join(self.image_path, f'page_{self.page + 1}' + '_image_' + str(count) + '.jpg'))
                count += 1
                
        except Exception as e:
            print('Could not get the image:', e)
            
    
    def _generate_uuid(self):
        '''Generate a unique identifier.'''
        print('Generating a unique identifier...')
        
        for u in range(len(self.sku_element)):
            uuid_Four = str(uuid.uuid4())
            self.product_data_container.uuidFour.append(uuid_Four)
 
        
    def _get_price(self):
        '''It gets the price of a product from the website.'''
        print('Get the price of a product from the website')
        
        price_element = self.driver.find_elements(by=By.XPATH, value=Config.XPATH_PRICES)
        print(len(price_element))
        
        for price in price_element:  
            
            if price == None:
                price = 'Empty'
                self.product_data_container.price_list.append(price)
            else:
                self.product_data_container.price_list.append(price.text)
        print(self.product_data_container.price_list)
       
    # def get_products(self):
    #     return self.driver.find_elements(by=By.CSS_SELECTOR, value=".s-main-slot .s-result-item")
        
    def _get_sku(self):
        '''It gets the sku from the website.'''
        print('Get the sku from the website...')
            
        self.sku_element = self.driver.find_elements(by=By.XPATH, value=Config.XPATH_SKU)
        print(len(self.sku_element))
        
        for sku in self.sku_element:  
            
            if sku.text == None:
                sku.text = 'Empty'
                self.product_data_container.sku_list.append(sku.text)
            else:
                self.product_data_container.sku_list.append(sku.text)
                
        
    def _get_asin(self):
        '''It gets the asin of the product from the website.'''
        print('Get the asin of the product from the website')
                    
        asin_element = self.driver.find_elements(by=By.XPATH, value=Config.XPATH_ASIN)
        print(len(asin_element))
        
        for asin in asin_element:  
                
            if asin.get_attribute('data-asin') == None:
                asin = 'Empty'
                self.product_data_container.asin_list.append(asin)
            else:
                self.product_data_container.asin_list.append(asin.get_attribute('data-asin'))
            
        
    def _get_reviews(self):
        '''It gets the number of reviews.'''
        print('Get the number of reviews...')
                    
        reviews_element = self.driver.find_elements(by=By.XPATH, value=Config.XPATH_REVIEWS)
        print(len(reviews_element))
        
        for reviews in reviews_element:  
            
            if reviews == None:
                reviews = 'Empty'
                self.product_data_container.reviews_list.append(reviews)
            else:
                self.product_data_container.reviews_list.append(reviews.text)
            

    def _get_image_link(self):
        '''It gets image links.'''
        print('Get image links...')
       
        image_link_element = self.driver.find_elements(by=By.XPATH, value=Config.XPATH_IMAGE_LINK)
        print(len(image_link_element))
        
        for image_link in image_link_element:  
            
            if image_link.get_attribute('src') == None:
                image_link = 'Empty'
                self.product_data_container.image_link_list.append(image_link)
            else:
                self.product_data_container.image_link_list.append(image_link.get_attribute('src'))
     
     
    def _get_product_link(self):
        '''It gets the product links.'''
        print('Get product links...')
                            
        product_link_element = self.driver.find_elements(by=By.XPATH, value=Config.XPATH_PRODUCT_LINK)
        print(len(product_link_element))
        
        for product_link in product_link_element:  
            
            if product_link.get_attribute('href') == None:
                product_link = 'Empty'
                self.product_data_container.product_link_list.append(product_link)
            else:
                self.product_data_container.product_link_list.append(product_link.get_attribute('href'))
            
                
    def _save_data(self):
        '''It saves the data preferably json or excel file.'''
        print("It is saving the data.")
        
        # print(self.product_data_container.to_json())
        
        product_data_info = {'price': self.product_data_container.price_list,
                             'sku': self.product_data_container.sku_list,
                             'asin': self.product_data_container.asin_list, 
                             'reviews': self.product_data_container.reviews_list, 
                             'product_link': self.product_data_container.product_link_list, 
                             'image_link': self.product_data_container.image_link_list,
                             'uuid': self.product_data_container.uuidFour
                             }
        
        df = pd.DataFrame.from_dict(product_data_info, orient='index')
        df = df.transpose()
        df.to_excel('iPhone13.xlsx', index=False, header=True, encoding='utf-8')
        
    def scrape_data(self):
        '''It scrapes all the data...'''
        print('Scraping all the data...')
        
        # self._create_images_folder()
        
        for self.page in range(self.num_page):
            
            print(f'Page: {self.page + 1}')
            
            # product_list = self.get_products()
            
            # for product in product_list:
                
            # self._download_images()
            self._get_price()
            self._get_sku()
            self._get_asin()
            self._get_reviews()
            self._get_image_link()
            self._get_product_link()
            self._generate_uuid()
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