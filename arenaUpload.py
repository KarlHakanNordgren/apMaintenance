#############################################
#############################################
# libraries

import subprocess # for system calls
import signal # for kill signal
import os # for system calls
from selenium import webdriver # for webdriving
import re # for finding text in webpages

#############################################
#############################################
#

driver = webdriver.Firefox()

driver.get('https://secure.advicepro.org.uk/v5alt/Home/Index')
UserNameElements = driver.find_elements_by_id('UserName')

if len(UserNameElements) > 0:
    driver.find_element_by_id('UserName').send_keys('hnordgren')
    driver.find_element_by_id('Password').send_keys('Advicepro4dvicepro')
    driver.find_element_by_xpath('//*[@id="logonPanel"]/form/fieldset/p/input').click()

errorsPage = driver.find_elements_by_class_name('validation-summary-errors')

while len(errorsPage) > 0:
    driver.get('https://secure.advicepro.org.uk/')
    driver.find_element_by_id('Username').send_keys('hnordgren')
    driver.find_element_by_id('Password').send_keys('Advicepro4dvicepro')
    driver.find_element_by_id('btnLogin').click()
    errorsPage = driver.find_elements_by_class_name('validation-summary-errors')

driver.find_element_by_link_text('Reports').click()
driver.find_element_by_link_text('Client Import').click()

mainWindowHandle = driver.window_handles

driver.find_element_by_id("beginImport").click()

for handle in driver.window_handles:
    if handle != mainWindowHandle:
        popupWindowHandle = handle
    else:
        continue

driver.switch_to.window(popupWindowHandle)

driver.find_element_by_xpath('//*[@id="importFile"]').send_keys('/Users/simon.walne/work/apMaintainance/datasets/tenantData.csv')

driver.find_element_by_link_text('Start Import')


print(driver.window_handles)

driver.find_element_by_link_text('Log Out').click()

driver.close()

'''

elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

'''
