from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

class amazon:
    
    def __init__(self):
        '''Initializing webscaraper...'''
        website = "https://www.amazon.co.uk/"
        opt = webdriver.ChromeOptions()
        opt.headless = True
        opt.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
        self.driver.get(website)
        self.driver.implicitly_wait(10)
        
    def accept_cookies(self):   
        '''Accepts cookies...'''     
        xpath_accept_cookies = "//input[@type='submit' and @id='sp-cc-accept']"
        accept_button = self.driver.find_element(By.XPATH, xpath_accept_cookies)
        accept_button.click()
        
    def download_images(self):
        '''Downloading images...'''
        
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
        
        
        
        # Beautiful Soup
        # soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        # results = soup.find_all("div", {"class": "a-section a-spacing-none s-padding-right-small s-title-instructions-style"}) 
        # l = len(results)
        # print(l)
        
        # item = results[0]
        # rating_tag = item.h2.a
        # description_tag = rating_tag.text.strip()
        # print(description_tag)
        # url = "https://www.amazon.co.uk" + rating_tag.get('href')
        # print(url)
        
        # price = item.find('span', 'a-price')
        # phone_price = price.find('span', 'a-offscreen').text
        # print(phone_price)
        
if __name__ == "__main__":  
    '''Main function...'''
    amz = amazon()
    amz.accept_cookies()     
    amz.search()

    amz.driver.close()
    amz.driver.quit()