from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_cap={"automationName":"Appium","platformName":"Android","deviceName":"cd046813",
             "appPackage":"com.android.settings","appActivity":"com.android.settings.Settings"}


driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)

#Function for validation
def val():
    try:
        #Enter the element selector for the object which you want to select
        driver.find_element(AppiumBy.ID,"com.android.dialer:id/main_options_menu_button")

        #Return True if the ID is Valid
        return True
    except:
        #Return False if the ID is Invalid
        return False
res=val()
print(res)