from selenium import webdriver 
import time 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/jbateman/Documents/Python Packages/chromedriver_win32 (1)/chromedriver.exe")

driver.set_page_load_timeout("10")
driver.get("https://www.bing.com")
time.sleep(3)
driver.find_element_by_id("sb_form_q").send_keys("Test")
driver.find_element_by_id("sb_form_q").send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()