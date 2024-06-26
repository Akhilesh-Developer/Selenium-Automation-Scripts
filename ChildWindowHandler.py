import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
time.sleep(2)

# now to get any data from another tab(child tab) we have to swich our driver to that tab because currently our driver is in parent tab scope.
tabs = driver.window_handles   # window_handles is a mehtod which hane a property of getting the names of all the window(tabs) that are opened
driver.switch_to.window(tabs[1])    # here we have successfully moved to another window
new_win_text = driver.find_element(By.TAG_NAME,"h3").text
print(new_win_text)