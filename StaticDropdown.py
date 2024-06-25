import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# In Static dropdowns we use Select class provided by Selenium to select the options

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))   # Now as we are using class so we have to create its object to use it
dropdown.select_by_visible_text("Female")     # There are a lot of ways to select options in static dropdown
time.sleep(5)
driver.close()