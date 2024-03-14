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
        merge_tj_act = data.get("merge_tj_files")
        merge_fr_act = data.get("merge_fr_files")
        print('this is  ok')
        if merge_tj_act == "merge_tj_act":
            print('this is not ok')
            file1 = data.get("file1")
            file2 = data.get("file2")
            df_report= pd.read_excel(file1)
            df_factors = pd.read_excel(file2)
            # print(df1)
            # print(df2)
            df_factors = df_factors.loc[df_factors[tjCol.factor_date]>"1399/11/22"]
            thisIndex = giroc(df_report)
            ls_data = []
            while len(df_report):
                mobile = df_report.iat[0,thisIndex.mobile]
                if len(df_factors.loc[df_factors[tjCol.mobile]== mobile]):
                    name = df_report.iat[0,thisIndex.name]
                    ls_data.append({roc.mobile:mobile, roc.name:name})
                df_report = df_report.loc[df_report[roc.mobile]!=mobile]
            dfData = pd.DataFrame(ls_data)
            dfData.to_excel("final_data.xlsx",index=False)
        if merge_fr_act == "merge_fr_act":
            print('this is  merge_fr_act')
            file1 = data.get("file_fr1")
            file2 = data.get("file_fr2")
            df_report= pd.read_excel(file1)
            
            df_sales = pd.read_excel(file2)
            # print(df1)
            # print(df2)
            df_sales = df_sales.loc[df_sales[tjCol.factor_date]>"1400/11/24"]
            df_sales = df_sales.sort_values(by=frCol.factor_date,ascending=True)
            df_sales.drop_duplicates(subset = frCol.mobile,keep= 'last',inplace = True)
            thisIndex = giroc(df_report)
            ls_data = []
            frIndex = get_index_fr(df_sales)
            while len(df_report):
                mobile = df_report.iat[0,thisIndex.mobile]
                df_check = df_sales.loc[df_sales[tjCol.mobile]== mobile]
                if len(df_check):
                    name = df_report.iat[0,thisIndex.name]
                    product = df_check.iat[0,frIndex.product]
                    ls_data.append({roc.mobile:mobile, roc.name:name,frCol.product:product})
                df_report = df_report.loc[df_report[roc.mobile]!=mobile]
            dfData = pd.DataFrame(ls_data)
            dfData.to_excel("final_data_fr.xlsx",index=False)
        if action == "run":
            # driver = webdriver.Firefox()
            # print('this is ok')
            task_selector(atk.task_name.get_report_from_hesabro_link,report_link)
        # driver.get('http://aradpayamak.net')
            # driver.get("https://honeymoonatr.com")
                # for t in driver.title:
            # result = {"result":(f"عنوان سایت بارگزاری شده: {driver.title}") }
        else:
            print("stop")
            # driver.close()
        
        # return redirect(("arad/"))
    # message ={"messages":"test"}
    
    return render(request,'get_the_report/get_from_address.html',result)
def get_report(request):
    return render(request,'get_the_report/get_from_address.html')