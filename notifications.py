from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_cap={"automationName":"Appium","platformName":"Android","deviceName":"cd046813",
             "appPackage":"","appActivity":""}


driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
time.sleep(5)

driver.open_notifications()
