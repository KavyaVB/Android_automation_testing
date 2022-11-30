from appium import webdriver
import time

desired_cap={"automationName":"Appium","platformName":"Android","deviceName":"cd046813",
             "appPackage":"","appActivity":""}

#selenium act as a client and send command to appium server via json protocol
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
time.sleep(5)

driver.toggle_wifi()

driver.toggle_location_services()

#prints session id
#print(driver.session_id)

#driver.set_power_capacity(20)

