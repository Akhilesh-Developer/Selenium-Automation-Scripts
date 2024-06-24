import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.linkedin.com/home")
driver.find_element(By.LINK_TEXT, "Sign in with email").click()
driver.find_element(By.XPATH, "//input[@type = 'text']").send_keys("akhileshtrader007@gmail.com")  # X Path - //input[@name = 'session_password']
driver.find_element(By.XPATH, "//input[@type = 'password']").send_keys("Since@11@22")
driver.find_element(By.XPATH, "//button[@type = 'submit']").click()






















time.sleep(10)