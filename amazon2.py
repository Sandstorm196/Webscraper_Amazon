from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import urllib
import wget
import socket
import ssl

class amazon:
    
    def __init__(self):
        '''Initializing webscaraper...'''
        website = "https://www.amazon.co.uk/"
        opt = webdriver.ChromeOptions()
        opt.headless = True
        opt.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
        # self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
        self.driver.get(website)
        self.driver.implicitly_wait(10)
        
    def accept_cookies(self):   
        '''Accepts cookies...'''     
        xpath_accept_cookies = "//input[@type='submit' and @id='sp-cc-accept']"
        accept_button = self.driver.find_element(By.XPATH, xpath_accept_cookies)
        accept_button.click()
        
    def search(self):        
        '''Searching for the product in the Amazon website.'''
        search_term = "iPhone 13"
        xpath_search = "//input[@id='twotabsearchtextbox']"
        search_input = self.driver.find_element(By.XPATH, xpath_search)
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.RETURN)

        xpath_click_apple = "//span[text()='Apple']"
        accept_button = self.driver.find_element(By.XPATH, xpath_click_apple)
        accept_button.click()
        
        img = self.driver.find_elements(by=By.XPATH, value="//img[@class='s-image']")
        print(len(img))

        src = [i.get_attribute('src') for i in img]
        print(len(src))
        
        image_path = os.getcwd()
        image_path = os.path.join(image_path, 'images')
        if not os.path.exists(image_path):
            os.mkdir(image_path)
            print(image_path)

        count = 0
        for i in enumerate(image_path):
            try:
                if src != None:
                    src = str(src)
                    print(src)
                  
                    for i in src:
                        save_as = os.path.join(image_path, 'image' + str(count) + '.jpg')
                        wget.download(i, save_as)     
                        count += 1    
                    # urllib.request.urlretrieve(src, os.path.join(image_path, str(count) + '.gif'))
                else:
                    raise TypeError
            except Exception as e:
                print(f'The error is {e}')
if __name__ == "__main__":  
    '''Main function...'''
    amz = amazon()
    amz.accept_cookies()     
    amz.search()

    amz.driver.close()
    amz.driver.quit()