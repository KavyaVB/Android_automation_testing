from appium import webdriver
import time

desired_cap={"automationName":"Appium","platformName":"Android","deviceName":"cd046813",
             "appPackage":"","appActivity":""}


driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
time.sleep(5)

driver.get_screenshot_as_file('scn.png')

#print(driver.capabilities)

driver.save_screenshot('scn1.png')