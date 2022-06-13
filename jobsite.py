import requests
from selenium import webdriver
import uuid
import os
import time
import pandas as pd
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class Jobsite():
    '''
    This class represents the jobsite.
    It contains the methods to scrape the data from the website.
    '''

    def __init__(self):
        '''
        Initialize the webdriver and the url.
        Chrome options are used to disable the notification pop-up.
        '''
        
        print("Options are initialized...")

        self.NoneType = type(None)

        self.opt = webdriver.ChromeOptions()
        self.opt.headless = True
        self.opt.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
        self.driver.get('https://www.jobsite.co.uk/')
        self.driver.implicitly_wait(10)
        
        self.images = []
        self.job_results = []
        
    def search(self,):
        '''
        This method searches for the job on the main page:
        - Select the job title
        - Select the job location
        - Select how far you want to travel
        '''
        
        print("Searching for the job...")

        cookie= self.driver.find_element_by_xpath('//div[@id="ccmgt_explicit_accept"]')

        try:
            cookie.click()
        except:
            pass 

        job_title = self.driver.find_element_by_id('keywords')
        job_title.click()
        job_title.send_keys('Data Scientist')
        time.sleep(1)

        location = self.driver.find_element_by_id('location')
        location.click()
        location.send_keys('London')
        time.sleep(1)

        dropdown = self.driver.find_element_by_id('Radius')
        radius = Select(dropdown)
        radius.select_by_visible_text('30 miles')
        time.sleep(1)

        search = self.driver.find_element_by_xpath('//input[@value="Search"]')
        search.click()
        time.sleep(2)
        
    def add_uuid(self,):
        '''
        This method adds a uuid to the job posting.
        '''
        
        print("Adding uuid to the job posting...")

        object_uuid = []
        for i in range(25):
            uuidFour = str(uuid.uuid4())
            object_uuid.append(uuidFour)
            print("uuid of version four", uuid)

    def download_images(self,):
        '''
        Download the images from the job posting.
        '''
        
        print("Downloading the images...")  
        
        elements = self.driver.find_elements_by_xpath('//div[@class="sc-fznxsB eaghqC"]/a/img')

        for i in elements:
            image = i.get_attribute('src')
            self.images.append(image)
            
        for image in self.images:
            if image is not None:
                file_name = image.split('/')[-1]
                print(f"The file name for images is:{file_name}")
                r = requests.get(image, stream=True)
                if r.status_code == 200:
                    with open(file_name, 'wb') as f:
                        for chunk in r:
                            f.write(chunk)
                else:
                    print("Unable to download image")
            else:
                print("Image is None")

        # images = [image.get_attribute('src') for image in images]
        # image_path = os.getcwd()
        # image_path = os.path.join(image_path, 'images')
        # os.mkdir(image_path)
        # print(image_path)

    def scrape_data(self):
        '''
        It scrapes the data from the job posting.
        '''
        
        print("Scraping the data...")
        
        for k in range(1):
            titles = self.driver.find_elements_by_xpath('//div[@class="sc-fzooss kBgtGS"]/a/h2')
            location = self.driver.find_elements_by_xpath('//li[@class="sc-fznXWL hSqkJy"]')
            salary = self.driver.find_elements_by_xpath('//dl[@class="sc-fzoJMP jpodhy" and @data-at="job-item-salary-info"]')
            company = self.driver.find_elements_by_xpath('//div[@class="sc-fzoiQi kuzZTz"]')
            posted = self.driver.find_elements_by_xpath('//ul[@class="sc-fznLxA bAwAgE"]/li[2]')
            description = self.driver.find_elements_by_xpath('//div[@class="sc-fzoYkl kSkZOQ"]/a/span')
            image_link = self.driver.find_elements_by_xpath('//div[@class="sc-fznxsB eaghqC"]/a/img')
            job_ref = self.driver.find_elements_by_xpath('//div[@class="sc-fzoYkl kSkZOQ"]/a')

            if not self.NoneType in [titles, location, salary, company, posted, description, image_link, job_ref]:
                for i in range(len(titles)):
                        data = {'Job_title': titles[i].text, 'Location': location[i].text, 'Salary': salary[i].text, 'Company': company[i].text, 'Post_Date': posted[i].text, 'Description': description[i].text, 'Image': image_link[i].get_attribute('href'), 'Job_Reference': job_ref[i].get_attribute('href')}
                        self.job_results.append(data)
            # with open('Data_Scientist_London.csv', 'a') as file:
            #     for i in range(len(titles)):
            #         file.write(titles[i].text + ";" + location[i].text + ";" + salary[i].text + ";" + company[i].text + ";" + posted[i].text+ ";" +
            #                   description[i].text + ";" + image_link[i].get_attribute("src") + ";" + job_ref[i].get_attribute("href") + "\n")

                # next=driver.find_element_by_xpath('//a[@title="Next"]')
                # next.click()
            df_data = pd.DataFrame(self.job_results, columns=['Job_title', 'Location', 'Salary', 'Company', 'Post_Date', 'Description', 'Image', 'Job_Reference'])
            print(df_data)
            df_data.to_excel('Data_Scientist_London.xlsx', index=False)
            df_data.to_json('Data_Scientist_London.json', orient='records')
            
            
            self.driver.close()
            self.driver.quit()
            
            
if __name__ == '__main__':
    jobsite = Jobsite()
    jobsite.search()
    jobsite.add_uuid()
    jobsite.download_images()
    jobsite.scrape_data()