from itertools import count
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

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(Constants.URL)

# opt = webdriver.ChromeOptions()
# opt.headless = False
# opt.add_argument("--headless")
# opt.add_argument("--disable-notifications")
# opt.add_argument("--disable-dev-shm-usage")
# opt.add_argument("--disable-gpu")
# opt.add_argument( "--no-sandbox")
# opt.add_argument("--disable-setuid-sandbox",)
# opt.add_argument('--ignore-certificate-errors')
# opt.add_argument("--test-type")
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
# driver.get(Constants.URL)
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

img = driver.find_elements(by=By.XPATH, value='//div[@class="sc-fznxsB eaghqC"]/a/img')
print(len(img))

src = [i.get_attribute('src') for i in img]
print(len(src))
print(src)

src_links = []
for i in range(len(src)):
    data = {'src': src[i], 'id': str(uuid.uuid4())[i]}
    src_links.append(data)
    df_data = pd.DataFrame(src_links, index=[i])
    df_data.to_json('Src_links.json', index=True)

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
            
            urllib.request.urlretrieve(src, os.path.join(image_path, str(count) + '.gif'))
        else:
            raise TypeError
    except Exception as e:
        print(f'The error is {e}')


driver.close()




