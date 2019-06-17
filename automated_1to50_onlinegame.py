import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#Make sure your chrome binary is at the correct location , in this case it is in the same level of this script

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")


browser = webdriver.Chrome(executable_path = DRIVER_BIN)


# The game is hosted in below url

browser.get('http://zzzscore.com/1to50/en')

# time.sleep(3)

nextButton = browser.find_element_by_id('grid')
nextButton.click()


#xpath
element_list = browser.find_elements_by_xpath("//div[contains(@style,'opacity: 1;')]")# to find all div elements with style= "opacity: 1;"

#css selector
#element_list = driver.find_elements_by_css_selector("[style^=opacity]") # to match divs containing style attribute starting with opacity


# print (element_list)


count = 1
flag = 0

for i in range(1,50):
    if flag is 1:
        # print ("Inside flag condiditon")
        break
    for items in element_list:
        # print (items.text)  #to print out element text
        # print(items.text)
        n = int(items.text)

        if n is count:
            # print("inside")
            items.click()
            count +=1
            if count > 27:
                flag=1
                break

# The tricky part in the Game is after 27 element the grid re appears , so we need to fetch the elements again


element_list_2 = browser.find_elements_by_xpath("//div[contains(@style,'opacity: 1;')]")# to find all div elements with style= "opacity: 1;"


for i in range(1,50):
    for items_2 in element_list_2:
        # print (items.text)  #to print out element text
        # print(items_2.text)
        try:
            n = int(items_2.text)
        except:
            # print("inside except block")
            pass

        if n is count:
            # print("inside")
            items_2.click()
            count +=1
            if count > 50:
                # print("game Over")
                break





