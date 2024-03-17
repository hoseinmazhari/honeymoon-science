import time
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from selenium import webdriver
# some_file.py
# import sys
# # caution: path[0] is reserved for script path (or '' in REPL)
# sys.path.insert(1, r'C:/honeymoon_project/selenium/hesabro/settings')
import os,sys
sys.path.append("..")
from selenium_files.settings.run_app import run_hesabro
from selenium_files.settings.run_app import task_selector
from selenium_files.settings import app_tasks as atk
def timeCheck()->bool:
    import time
    thisTime = time.ctime()
    # print (thisTime)
    firstColon = thisTime.find(":")
    # print(firstColon)
    thisTime = thisTime[firstColon-2:firstColon+6]
    # print(thisTime)
    if thisTime>"10:00:00" and thisTime< "11:00:00":
        
        return True
    else:
        return False
# from selenim_files.hesabro.datpaa.user_
# from selenium.
# os.path.abspath(os.path.join(os.getcwd(), '...'))
# from .honeymoon_project.sel
# import 
# from ...selenium_files.hesabro.settings.run_app import run_hesabro
def update_db(request):
    # print("this is test")
    result = {"result":"stoped"}
    if request.method == 'POST':
        data = request.POST
        action = data.get("act")
        sms_text = data.get("sms_text")
        if action == "run":
            # driver = webdriver.Firefox()
            if timeCheck():
                task_selector(atk.task_name.update_birthday,sms_text)
        # driver.get('http://aradpayamak.net')
            # driver.get("https://honeymoonatr.com")
                # for t in driver.title:
            # result = {"result":(f"عنوان سایت بارگزاری شده: {driver.title}") }
        else:
            print("stop")
            # driver.close()
        
        # return redirect(("arad/"))
    # message ={"messages":"test"}
    
    return render(request,'birthday/update_birthday_db.html',result)
def birthday_page(request):
    # 
    return render(request,'birthday/birthday_page.html')
def arad_detail(request):
    
    for i in range(20):
        print(i)
    driver = webdriver.Firefox()
    # driver.get('http://aradpayamak.net')
    driver.get("https://honeymoonatr.com")
        # for t in driver.title:
    result = (f"عنوان سایت بارگزاری شده: {driver.title}")  
    
    return render(request,"birthday/arad/arad_detail.html")