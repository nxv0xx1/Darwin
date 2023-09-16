import selenium
from selenium import webdriver
import time
browser = webdriver.chrome()
browser.get('google.com')
time.sleep(10)
feeling_lucky = webdriver.find_element("name", "btnI")
