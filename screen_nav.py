from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_cap={"automationName":"Appium","platformName":"Android","deviceName":"cd046813",
             "appPackage":"com.android.settings","appActivity":"com.android.settings.Settings"}


driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
#time.sleep(5)

def nav():

    #Click on wifi option
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Network & internet\")").click()
    time.sleep(5)

    #switch on the toggle button
    driver.find_element(AppiumBy.ID,"com.android.settings:id/switchWidget").click()
    time.sleep(5)

    #click on return symbol
    driver.find_element(AppiumBy.XPATH,"//android.widget.ImageButton[@index=0]").click()
    time.sleep(5)

    #close app
    #driver.close_app()

    #driver.launch_app()
    '''
    #click on other option
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Connected devices\")").click()

    #return
    driver.find_element(AppiumBy.XPATH,"//android.widget.ImageButton[@index=0]").click()
    time.sleep(5)
    '''
nav()
