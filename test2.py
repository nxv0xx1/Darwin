# Selenium for web driving
import selenium
from selenium import webdriver
driver = webdriver.Chrome()  

# Time for pausing between navigation
import time

# Talk to the browser 
browser = webdriver.Chrome()
browser.get('http://www.google.com')
# browser.get('http://192.168.188.1')
# webdriver.maximize_window()

# Select the password box
password_box = driver.find_element_by_id("txtpwd")

#typeInThePassword
password_box.send_keys('admin')

#findingAndClickingLoginButton
#login_button = driver.find_element_by_id('btnLogin')
#login_button.click()

#click on advanced



#closeBrowser
#browser.quit()
