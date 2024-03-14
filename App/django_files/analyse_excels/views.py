import time
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
# from selenium import webdriver

import os,sys
sys.path.append("..")
from python_files.codes.a00001_invoices import a0_1_invoices_Count
from python_files.file_types.excel_files import tjCol
from python_files.file_types.excel_files import getIndexTj
from selenium_files.settings.run_app import task_selector
from selenium_files.settings import app_tasks as atk

# from selenim_files.hesabro.datpaa.user_
# from selenium.
# os.path.abspath(os.path.join(os.getcwd(), '...'))
# from .honeymoon_project.sel
# import 
# from ...selenium_files.hesabro.settings.run_app import run_hesabro
def factors_count(request):
    # print("this is test")
    result = {"result":"stoped"}
    if request.method == 'POST':
        data = request.POST
        action = data.get("act")
        sms_text = data.get("sms_text")
        if action == "run":
            # driver = webdriver.Firefox()
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
def analyse_list(request):
    # 
    return render(request,'analyse_excels/analyse_list.html')
