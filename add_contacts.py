from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_cap={"automationName":"Appium","platformName":"Android","deviceName":"cd046813",
             "appPackage":"com.android.contacts","appActivity":"com.android.contacts.activities.PeopleActivity"}


driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
time.sleep(5)

def add_contact():

    #click on new contact option to create new contact using ACCESSIBILITY_ID(Content_desc)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Create new contact").click()
    time.sleep(5)

    #click on the storage option where you want to store the contacts using ID(Resource_ID)
    #driver.find_element(AppiumBy.ID,"com.android.contacts:id/left_button").click()

    #Enter the first name using UI Selector and set_text()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"First name\")").set_text("Kavya")

    #Enter the last name
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Last name\")").set_text("VB")

    #Enter the phone num
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Phone\")").set_value(76769110146)

    #Click on save button using ID(Resource_ID)
    driver.find_element(AppiumBy.ID,"com.android.contacts:id/editor_menu_save_button").click()
    time.sleep(5)

    driver.close_app()
add_contact()

