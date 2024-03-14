import requests
from ..hesabro.settings import xpath_hesabro as xph
from ..hesabro.settings import DateJuToJa as djtj
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from .xpath import get_xpath
from ..hesabro.settings.xpath import get_xpath
import time
import pandas as pd
import os
from selenium.webdriver.common.keys import Keys
# from .merchandise import search_fieldProduct
from ..hesabro.settings.browser import write_in_element
from ..hesabro.settings import app_address
from tqdm import tqdm
# from .test import dwn
class this_file_cols():
    mobile = "موبایل"
    name = "نام و نام خانوادگی"
    # birthday = "تاریخ تولد"
def download_data(driver, title, this_delay): 
    try:
        is_true = False
        # name = []
        # mobile = []
        # birthday = []
        lsData = []
        while is_true==False:
            
            try:
                element =driver.find_element(By.XPATH,xph.create_reportcustomer.dataReport.tbody)
                # element[1].click()
                trs = element.find_elements(By.TAG_NAME, "tr")
                for tr_index in trs:
                    tds = tr_index.find_elements(By.TAG_NAME, "td")
                    name=(tds[2].text)
                    name.replace("(موقت)", "")
                    birthday=(tds[4].text)
                    mobile=(tds[7].text)
                    lsData.append({this_file_cols.mobile : mobile, this_file_cols.name : name,
                                   this_file_cols.birthday : birthday})
                    data = pd.DataFrame(lsData)
                    data.to_excel(f"{title}.xlsx",index=False)
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(1.2)
                element =driver.find_element(By.XPATH,xph.create_reportcustomer.dataReport.next_p)
                if element.is_displayed():
                        element.click()
                        time.sleep(2)
                else:
                    is_true = True
                    # driver.close()
                # time.sleep(6)
            except Exception as e:
                print(e)
                is_true = True
            #     time.sleep(5)
            #     is_true = False
        data = pd.DataFrame(lsData)
        data.to_excel(f"{title}.xlsx",index=False)
        return data
            # element = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, xph.create_reportcustomer.download)))
    except Exception as e:
        print(e)
        is_true = False
    
def set_title(driver, current_url, title, this_delay):
    is_true = False
    counter = 0
    while is_true==False:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xph.create_reportcustomer.title)))
            element.click()
            write_in_element(title, element)
            is_true = True
        except:
            counter += 1
            if counter>20:
                driver.get(current_url)
                counter = 0
            is_true = False
            time.sleep(this_delay)

def set_birthdayfromday(driver,birthdayfromday,this_delay):
    
    is_true = False
    counter = 0
    while is_true==False:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xph.create_reportcustomer.birthdayfromday)))
            element.click()
            write_in_element(birthdayfromday, element)
            is_true = True
        except:
            counter += 1
            if counter>50:
                # counter = 0
                return is_true
            is_true = False
            time.sleep(this_delay)
    return is_true

def set_birthdaytoday(driver, birthdaytoday, this_delay):
    is_true = False
    while is_true==False:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xph.create_reportcustomer.birthdaytoday)))
            element.click()
            write_in_element(birthdaytoday, element)
            is_true = True
        except:
            is_true = False

            
def send_sms(driver,main_url,title): 
    #  1- تغییر آدرس مرورگر به صفححه ایجاد گزاشات
    this_address = app_address.urls["birthday"]["create_rpt"]
    driver.get(this_address)
    while driver.current_url != this_address: # جهت اطمینان از باز شدن صفحه ی درخواست شده در گزینه 1 از حلقه استفاده شده است
        driver.get(this_address)
        time.sleep(3)
    
    # 2- جهت استخراج تاریخ جاری و استفاده از آن در برنامه از این قسمت استفاده شده است
    this_date = str(djtj.todaydate()).replace("/","-")

    # 3- جهت جدا نمودن روز تاریخ جاری از این قسمت استفاده شده است
    birthdayfromday = birthdaytoday = this_date[-2:]
    # birthdayfromday = birthdaytoday = "2"

    # 4- از این قسمت برای جدا کردن ماه تاریخ جاری استفاده شده است
    birthdaymonth = birthdaytomonth = this_date[-5:-3]

    # 5- جهت تعیین عنوان گزارش از این قسمت استفاده شده است
    title = f"{title} {this_date}"

    this_delay = 6
    # 6-  جهت کلیک روی گزینه ایجاد گزارش از این گزینه استفاده شده است
    # نکته: از شمارنده برای اطمینان از عدم پگینیشن بودن وضعیت سایت استفاده شده است
    is_true = False
    counter = 0
    while is_true==False:
        
        try:
            element =driver.find_elements(By.XPATH,xph.create_reportcustomer.btn_createRpt)
            element[1].click()
            is_true = True
        except:
            counter += 1
            if counter>20:
                driver.get(this_address)
                counter = 0
            is_true = False
            time.sleep(this_delay)

    # 7- از این قسمت برای ذخیره آدرس مربوط به ایجاد گزارش استفاده شده است تا در صورت نیاز مجدد بارگزاری شود
    current_url = driver.current_url
    
    # 8- از این قسمت برای درج عنوان استفاده شده است
    set_title(driver, current_url, title, this_delay)
    # is_true = False
    # while is_true == False:
    is_true = set_birthdayfromday(driver, birthdayfromday, this_delay)

    set_birthdaytoday(driver, birthdaytoday,this_delay)
    
    
        
    is_true = False
    while is_true==False:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xph.create_reportcustomer.birthdaymonth)))
            element.click()
            time.sleep(2)
            element = element.find_elements(By.TAG_NAME,'option')
            element[int(birthdaymonth)].click()
            time.sleep(2)
            is_true = True
        except:
            is_true = False
    
    is_true =False
    while is_true==False:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xph.create_reportcustomer.birthdaytomonth)))
            element.click()
            time.sleep(2)
            element = element.find_elements(By.TAG_NAME,'option')
            element[int(birthdaytomonth)].click()
            time.sleep(2)
            is_true = True
        except:
            is_true = False
    
    is_true = False
    while is_true==False:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xph.create_reportcustomer.save)))
            element.click()
            # write_in_element(birthdaytoday, element)
            is_true = True
        except:
            is_true = False
    time.sleep(3)
    dfData = download_data(driver, title, this_delay)
    return dfData


