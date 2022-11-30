from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_cap = {"automationName": "Appium", "platformName": "Android", "deviceName": "GUFMWCUGV4LR7SJB",
               "appPackage": "", "appActivity": ""}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
time.sleep(5)

print(driver.current_activity)

print(driver.current_package)
'''
driver.start_activity('com.android.music','.MusicBrowserActivity')
'''
