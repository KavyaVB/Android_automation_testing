from appium import webdriver
import time

desired_cap={"automationName":"Appium","platformName":"Android","deviceName":"cd046813",
             "appPackage":"","appActivity":""}


driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
time.sleep(5)

def lock_dev():
    #func to lock the device
    driver.lock()

    #func to unlock
    driver.unlock()

    driver.stop_client()
lock_dev()

