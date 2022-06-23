'''Amazon scraper for iPhone - Constants'''

URL = "https://www.amazon.co.uk/"
SEARCH_TERM = "iPhone 13"

XPATH_COOKIES = "//input[@type='submit' and @id='sp-cc-accept']"
XPATH_SEARCH_BOX = "//input[@id='twotabsearchtextbox']"
XPATH_APPLE_BRAND = "//span[text()='Apple']"
XPATH_IMAGES = "//img[@class='s-image']"
XPATH_SKU = "//span[contains(@class,'a-size-medium a-color-base a-text-normal')]"
XPATH_ASIN = "//div[contains(@class, 's-result-item s-asin')]"
XPATH_REVIEWS = "//div[@class='a-row a-size-small']/span[2]"
XPATH_IMAGE_LINK = "//img[@class='s-image']"
XPATH_PRODUCT_LINK = "//a[@class='a-link-normal s-no-outline']"
XPATH_PRICES = "//span[contains(@class,'price-whole')]"
XPATH_NEXT_PAGE = "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']"