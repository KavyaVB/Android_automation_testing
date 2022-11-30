from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_cap={"automationName":"Appium","platformName":"Android","deviceName":"55fc7c16",
             "appPackage":"com.android.contacts","appActivity":"activities.PeopleActivity"}


driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
time.sleep(5)

def delete_contact():

    #Click on the contact which you want to delete
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Kavya VB").click()

    #click on more options using Accessibility_ID(Resource_ID)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,"More options").click()

    #click on Delete option using UI Selector
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Delete\")").click()

    #click on return option to exit the page
    driver.find_element(AppiumBy.ID,"android:id/button1").click()
    time.sleep(5)

    driver.close_app()
delete_contact()