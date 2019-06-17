from selenium import webdriver
import os
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


#Make sure your chrome binary is at the correct location , in this case it is in the same level of this script

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

browser = webdriver.Chrome(executable_path = DRIVER_BIN)

# To vote for a contestant we need to login to gmail 

browser.get('http://gmail.com')

emailElem = browser.find_element_by_id('identifierId')

# fill in your gmail user name 

emailElem.send_keys('replace_with_your_gmail_username')
nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()
time.sleep(3)


password = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))
)

# fill in your gmail password 

password.send_keys("replae_with_your_gmail_username")

browser.find_element_by_id("passwordNext").click()

time.sleep(8)

#open tab
browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
# You can use (Keys.CONTROL + 't') on other OSs

# Load a page
browser.get('https://www.google.co.in/search?q=big+boss+telugu+vote+2018&oq=big+b&aqs=chrome.0.69i59j69i57j69i59l2j69i61j69i60.1309j0j1&sourceid=chrome&ie=UTF-8')

elm = browser.find_element_by_css_selector("[data-id='bbtelugu201808kaushal']").click()

time.sleep(5)

browser.find_element_by_css_selector("[aria-valuemax='50']").click()
browser.find_element_by_css_selector(".fSXkBc").click()
browser.find_element_by_css_selector("[data-async-trigger='submit']").click()
