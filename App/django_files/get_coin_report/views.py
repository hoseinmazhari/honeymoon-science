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
import pandas as pd
from selenium_files.hesabro.club.fetch_report_data import report_output_cols as roc,get_index_report_output_cols as giroc
class tjCol():
    mobile = "موبایل"
    factor_date = "تاريخ"
class frCol():
    mobile = tjCol.mobile
    factor_date = tjCol.factor_date
    product = "عنوان کالا"
def get_index_fr(df):
    thisItter = -1
    thisClass = frCol()
    for col in df.columns:
        thisItter += 1
        if col == thisClass.mobile:
            thisClass.mobile = thisItter
        elif col == thisClass.factor_date:
            thisClass.factor_date = thisItter
        elif col == thisClass.product:
            thisClass.product = thisItter
    return thisClass
# Create your views here.
def get_report_from_hesabro(request):
    # print("this is test")
    result = {"result":"stoped"}
    if request.method == 'POST':
        print('this is  ok')
        data = request.POST
        action = data.get("act")
        report_link =(data.get("report_link")).strip()
        
        
        if action == "run":
            # driver = webdriver.Firefox()
            # print('this is ok')
            task_selector(atk.task_name.get_coin_report_from_hesabro_link,report_link)
        # driver.get('http://aradpayamak.net')
            # driver.get("https://honeymoonatr.com")
                # for t in driver.title:
            # result = {"result":(f"عنوان سایت بارگزاری شده: {driver.title}") }
        else:
            print("stop")
            # driver.close()
        
        # return redirect(("arad/"))
    # message ={"messages":"test"}
    
    return render(request,'get_coin_report/get_from_address.html',result)
def get_report(request):
    return render(request,'get_coin_report/get_from_address.html')