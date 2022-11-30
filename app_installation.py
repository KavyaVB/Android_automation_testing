from appium import webdriver
import time

desired_cap={"automationName":"Appium",
             "platformName":"Android",
             "deviceName":"GUFMWCUGV4LR7SJB",
             "app":"C:/Users/Kavya VB/Downloads/Skype_v8.88.0.404_apkpure.com.apk",
             "appPackage":"","appActivity":""}


driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
time.sleep(5)

if "app" in desired_cap:
    print('installed')
else:
    print('native')

def app_install():
    #Install the application using the apk path which is pre downloaded in the system
    driver.install_app("C:/Users/Kavya VB/Downloads/Skype_v8.88.0.404_apkpure.com.apk")
app_install()

