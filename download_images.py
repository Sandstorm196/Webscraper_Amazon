import io
import shutil
import ssl
from types import NoneType
import certifi
import requests
import Constants
import uuid
import os
import wget 
import time
import pandas as pd
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import urllib
import urllib.parse
from PIL import Image


options = Options()
options.headless = True
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(Constants.URL)

driver.implicitly_wait(10)

cookie = driver.find_element(by=By.XPATH, value=Constants.COOKIE_XPATH)

try:
    cookie.click()
except Exception as e:
    print(e)

job_title = driver.find_element(by=By.ID, value='keywords')
job_title.click()
job_title.send_keys('Data Scientist')
time.sleep(1)

location = driver.find_element(by=By.ID, value='location')
location.click()
location.send_keys('London')
time.sleep(1)

dropdown = driver.find_element(by=By.ID, value='Radius')
radius = Select(dropdown)
radius.select_by_visible_text('30 miles')
time.sleep(2)

search = driver.find_element(by=By.XPATH, value=Constants.SEARCH_XPATH)
search.click()
# time.sleep(3)
driver.implicitly_wait(10)

logo_images = []

elements = driver.find_elements(by=By.XPATH, value='//div[@class="sc-fznxsB eaghqC"]')
print(len(elements))

if not NoneType in elements:
    for i in elements:
        image = i.get_attribute('src')
        logo_images.append(image)
    for img in logo_images:
        file_name = img.split('/')[-1]
        # print(file_name)
        r = requests.get(img, stream=True)
        if r.status_code == 200:
            with open(file_name, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
        else:
            print('Error: ', r.status_code)



    
# print(len(new_links))
# print(new_links)

# new_links = []

# for link in src_links:
#     split_link = link.split('//')
#     split_link[0] = 'http://' 
#     new_link = split_link[0] + split_link[1]    
#     new_links.append(new_link)
    
# print(new_links)
# print(len(new_links))


# image_path = os.getcwd()
# image_path = os.path.join(image_path, 'images')
# if not os.path.exists(image_path):
#     os.mkdir(image_path)
#     print(image_path)
    


# try: 
#     count = 0
#     for i in enumerate(image_path):
#             if new_links != None:
#                 new_links = str(new_links)
#                 print(new_links)
                
#                 urllib.request.urlopen(new_links, context=ssl.create_default_context(cafile=certifi.where()))
#                 # urllib.request.urlretrieve(new_links, os.path.join(image_path, str(count) + '.jpg'))
#             else:
#                 raise TypeError
# except Exception as e:
#     print(f'The error is {e}')


driver.close()




