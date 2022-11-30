import os

def start_server():
    #start server
    os.system("start /B start cmd.exe @cmd /k appium")
start_server()

def stop_server():
    #stop server
    os.system("taskkill /F /IM node.exe")
    os.system("taskkill /F /IM cmd.exe")
stop_server()