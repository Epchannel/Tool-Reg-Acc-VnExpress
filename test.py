#
# STANDARD selenium Chromedriver
#
from selenium import webdriver
chrome = webdriver.Chrome()
chrome.get('https://datadome.co/customers-stories/toppreise-ends-web-scraping-and-content-theft-with-datadome/')
chrome.save_screenshot('datadome_regular_webdriver.png')
True   # it caused my ip to be flagged, unfortunately


#
# UNDETECTED chromedriver (headless,even)
#
import undetected_chromedriver as uc
options = uc.ChromeOptions()
options.headless=True
options.add_argument('--headless')
chrome = uc.Chrome(options=options)
chrome.get('https://datadome.co/customers-stories/toppreise-ends-web-scraping-and-content-theft-with-datadome/')
chrome.save_screenshot('datadome_undetected_webddriver.png')