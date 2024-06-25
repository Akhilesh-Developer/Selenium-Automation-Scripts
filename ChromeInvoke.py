import time

from selenium import webdriver      # there is a class in selenium webdriver, the class name itself is webdriver
# from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()     #here you have successfully invoked Chrome browser  ---- here Chrome is a method applied on webdriver class with the help of object(driver)
         # webdriver is basically codes that includes diffrent methods to perform some functionality on browser, every browser have it's own web driver

# IMPORTANT - Chrome does not allow to be invoked directly with help of webdriver class, every versions of Chrome have it's driver service too which acts as a medium, webdriver class will first interact with browser's driver and then driver will convert commands to be executable by chrome, that's how it workes

# A lot of company uses VPN to ristrict the download of driver, in this case we have to download the driver manually.
# Service("")   # This is a service class in which you have to pass the path of driver download


driver.get("https://www.linkedin.com/in/akhilesh-tripathi-a89a90195/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
























time.sleep(5)