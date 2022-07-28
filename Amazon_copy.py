from dataclasses import dataclass, field
from tkinter import TRUE
from unittest import result
from dataclasses_json import dataclass_json
import uuid
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from sqlalchemy import create_engine
from botocore.exceptions import ClientError
# import boto3
import sqlalchemy
import os
import urllib
import pandas as pd
import Config_copy
import time
# import Credentials

@dataclass_json
@dataclass()
class Data:    
    
    price_list : list = field(default_factory=list) 
    sku_list : list = field(default_factory=list) 
    tech_properties_list : list = field(default_factory=list)
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
        self.driver.get(Config_copy.URL)
        self.driver.set_page_load_timeout(10)
        self.driver.implicitly_wait(10)
        self.num_page = 1
        self.product_data_container = Data()
        # self.engine = create_engine(f"{Credentials.DATABASE_TYPE}+{Credentials.DBAPI}://{Credentials.USER}:{Credentials.PASSWORD}@{Credentials.HOST}:{Credentials.PORT}/{Credentials.DATABASE}")
        # self.engine.connect()

        
    def accept_cookies(self):   
        '''Accepts cookies...'''     
        print("Accepting cookies...")
        
        time.sleep(2)
        try: 
            accept_button = self.driver.find_element(By.XPATH, Config_copy.XPATH_COOKIES)
            accept_button.click()
            time.sleep(2)
        except  NoSuchElementException as error:
            print("NoSuchElementException, cookies button has not been clicked:", error)
            pass

    def search(self):        
        '''Searching for the product in the Amazon website.'''
        print("Searching for the product...")
        
        search_input = self.driver.find_element(By.XPATH, Config_copy.XPATH_SEARCH_BOX)
        search_input.send_keys(Config_copy.SEARCH_TERM)
        search_input.send_keys(Keys.RETURN)
        time.sleep(2)
        

    def click_on_brand(self):
        time.sleep(2)
        accept_button = self.driver.find_element(By.XPATH, Config_copy.XPATH_APPLE_BRAND)
        accept_button.click()
        
        
    def create_images_folder(self):
        '''It creates the images folder.'''
        print('Creating images folder...')
        
        self.image_path = os.getcwd()
        self.image_path = os.path.join(self.image_path, 'iPhone_13_images')
        
        if not os.path.exists(self.image_path):
            os.mkdir(self.image_path)
                        
            
    def __download_images(self):
        '''Downloads images from the Amazon website with the given number of the page.'''
        print("Downloading images...")

        count = 1
        time.sleep(7)
        
        try:
            img_element = self.driver.find_elements(by=By.XPATH, value=Config_copy.XPATH_IMAGES)
            print(len(img_element))

            src = [image.get_attribute('src') for image in img_element]
            print(len(src))
            
            for i in src: 
                urllib.request.urlretrieve(i, os.path.join(self.image_path, f'page_{self.page + 1}' + '_image_' + str(count) + '.jpg'))
                count += 1
                
        except Exception as error:
            print('Could not get the image:', error)
            
            
    def __get_search_results(self):
        '''It gets the search results for the products.'''
        print("Get the search results for the products.")
        
        container = self.driver.find_element(By.CSS_SELECTOR, 'div.s-main-slot') 
        search_results = container.find_elements(By.XPATH, './/div[@class="a-section"]//a') 

        product_links = []
        for product in search_results:
            product_links.append(product.get_attribute("href"))
        print(len(product_links))
        
        all_products = []
        for product_link in product_links:
            print(type(product_link))
            try:
                if product_link.startswith('http://') or product_link.startswith('https://'):
                    self.driver.get(product_link)
                    all_products.append(self.__build_product_obj(Config_copy.product_xpath_dict))
                    print(all_products)
                
            except Exception as error:
                print("The error is: ",error)
                pass

        print(all_products)


    def __build_product_obj(self, product_xpath_dict: dict):
        '''It gets the all product information.'''
        print('Building product object...')

        for keys, values in product_xpath_dict.items():
            
                current_attribute = self.driver.find_element(By.CLASS_NAME, values).text
                setattr(self.product_data_container, keys, current_attribute)
                return self.product_data_container.price_list
            
              
    def __generate_uuid(self):
        '''Generate a unique identifier.'''
        print('Generating a unique identifier...')
        
        for u in range(len(self.product_data_container.sku_list)):
            uuid_Four = str(uuid.uuid4())
            self.product_data_container.uuidFour.append(uuid_Four)
                    
            
    def __save_to_rds(self):
        '''It saves the data from data class as json to the AWS RDS postgresql.'''
        print("The data has been saved to the AWS RDS postgresql.")
        
        data_json = self.product_data_container.to_json()        
        df = pd.read_json(data_json)
        print(df)
        # df.to_sql('iPhone13', self.engine, if_exists='replace')


    # def __upload_img_s3(self):
    #     '''It uploads the images, what have been scraped, to the Amazon S3 bucket.'''
    #     print("Uploading images to AWS S3...")
        
    #     s3_client = boto3.client('s3',
    #                       aws_access_key_id = Credentials.ACCESS_KEY_ID,
    #                       aws_secret_access_key = Credentials.SECRECT_ACCESS_KEY)
         
    #     images_folder = os.path.join(os.getcwd(), 'iPhone_13_images')
        
    #     for file in os.listdir(images_folder):
    #         if not file.startswith('~'):
    #             try:
    #                 print('Uploading file {0}...'.format(file))
    #                 s3_client.upload_file(
    #                     os.path.join(images_folder, file),
    #                     Credentials.BUCKET_NAME,
    #                     file)
                    
    #             except ClientError as error:
    #                 print(f'Credential is incorrect: {error}')
    #             except Exception as error:
    #                 print(f'Error: {error}')

        
    def _scrape_data(self):
        '''It scrapes all the data...'''
        print('Scraping all the data...')
        
        # self.create_images_folder()
        
        for self.page in range(self.num_page):
            
            print(f'Page: {self.page + 1}')
            
            
            # self._download_images()
            self.__get_search_results()
            self.__build_product_obj(Config_copy.product_xpath_dict)
            self.__generate_uuid()
        self.__save_to_rds()
        # self.__upload_img_s3()
            
        time.sleep(3)
        next = self.driver.find_element(by=By.XPATH, value=Config_copy.XPATH_NEXT_PAGE)
        next.click()
                
if __name__ == "__main__":  
    
    '''Main function...'''
    
    amz = Amazon()
    amz.accept_cookies()  
    amz.search()
    amz.click_on_brand()
    amz._scrape_data()

    amz.driver.close()
    amz.driver.quit()
    
    print("Done!")