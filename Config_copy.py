'''Amazon scraper for iPhone - Constants'''

URL = "https://www.amazon.co.uk/"
SEARCH_TERM = "iPhone 13"

XPATH_COOKIES = "//input[@type='submit' and @id='sp-cc-accept']"
XPATH_SEARCH_BOX = "//input[@id='twotabsearchtextbox']"
XPATH_APPLE_BRAND = "//span[text()='Apple']"

# They require .text
product_xpath_dict = {"price_list" : "a-price-whole"
                    #   "sku_list" : ".//span[contains(@class,'a-size-medium a-color-base a-text-normal')]",
                    #   "tech_properties_list" : ".//div[contains(@class, 's-result-item s-asin')]",
                    #   "reviews_list" : ".//div[@class='a-row a-size-small']/span[2]",
                    #   "price_list": ".//span[contains(@class,'a-price-whole')]"
                      }

# They require .get_attribute('src') and .get_attribute('href') 
# "image_link_list" : ".//img[@class='s-image']",
# "product_link_list" : ".//a[@class='a-link-normal s-no-outline']"

XPATH_IMAGES = "//img[@class='s-image']"
# XPATH_SKU = ".//span[contains(@class,'a-size-medium a-color-base a-text-normal')]"
# XPATH_ASIN = ".//div[contains(@class, 's-result-item s-asin')]"
# XPATH_REVIEWS = ".//div[@class='a-row a-size-small']/span[2]"
# XPATH_IMAGE_LINK = ".//img[@class='s-image']"
XPATH_PRODUCT_LINK = ".//a[@class='a-link-normal s-no-outline']"
# XPATH_PRICES = ".//span[contains(@class,'a-price-whole')]"
XPATH_NEXT_PAGE = "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']"

# container = self.driver.find_element(By.CSS_SELECTOR, 'div.s-main-slot') 
# search_results = container.find_elements(By.XPATH, './/div[@class="a-section"]')