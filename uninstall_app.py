from appium import webdriver
import time

desired_cap={"automationName":"Appium","platformName":"Android","deviceName":"cd046813",
             "appPackage":"","appActivity":""}


driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
time.sleep(5)

driver.remove_app('com.bsbportal.music')

