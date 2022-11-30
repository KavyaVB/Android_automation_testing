from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_cap={"automationName":"Appium","platformName":"Android","deviceName":"cd046813",
             "appPackage":"com.android.settings","appActivity":"com.android.settings.Settings"}


driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
time.sleep(5)

#let the application run in background for particular period of time
driver.background_app(5)
#driver.background_app(-1)



