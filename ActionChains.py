import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)     # we have to give implicit wait so that every component takes their time to load completely.
driver.maximize_window()
mouse = ActionChains(driver)     # ActionChains is a class to perform mouse activity
mouse.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
mouse.context_click(driver.find_element(By.XPATH, "//a[text() = 'Top']")).perform()   # I can use link Text also - By.LINK TEXT,'Top'
mouse.move_to_element(driver.find_element(By.XPATH,"//a[text() = 'Reload']")).click().perform()
