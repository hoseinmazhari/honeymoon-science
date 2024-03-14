# import requests
from ...settings import xpath_hesabro as xph
from ...settings import DateJuToJa as djtj
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from .xpath import get_xpath
from ...settings.xpath import get_xpath
import time
import pandas as pd
import os

from selenium.webdriver.common.keys import Keys
# from .merchandise import search_fieldProduct
from ...settings.browser import write_in_element
from ...settings import app_address
# from tqdm import tqdm
# from .test import dwn
class report_output_cols():
    # mobile = "موبایل"
    
    name = "نام و نام خانوادگی"
    useCount = "تعداد استفاده"
    mod = "مانده"
    id = "آیدی"
def get_index_report_output_cols(df):
    thisClass = report_output_cols()
    thisItter = -1
    for col in df.columns:
        thisItter += 1
        if col == thisClass.name:
            thisClass.name = thisItter
        elif col == thisClass.mod:
            thisClass.mod = thisItter
        elif col == thisClass.useCount:
            thisClass.useCount = thisItter
        elif col == thisClass.id:
            thisClass.id = thisItter
    return thisClass
def download_data(driver, title, this_delay): 
    try:
        is_true = False
        # name = []
        # mobile = []
        # birthday = []
        lsData = []
        counter = 0
        while is_true==False:
            counter += 1
            
            try:
                print("find  table")
                element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xph.create_coin_report_hesabro.tbl)))
                # element.click()
                element = element.find_element(By.TAG_NAME, "tbody")
                print("find tbody table ok")
                # element =driver.find_element(By.XPATH,xph.create_reportcustomer.dataReport.tbody)
                # element[1].click()
                # trs = WebDriverWait(driver, 10).until(
                # EC.presence_of_elements_located((By.TAG_NAME, "tr")))
                # elem
                trs = element.find_elements(By.TAG_NAME, "tr")
                print("find tr is ok")
                for tr_index in trs:
                   
                    tds = tr_index.find_elements(By.TAG_NAME, "td")
                    print("find td is ok")
                    rw = (tds[0].text)
                    print("find row is ok")
                    id = (tds[1].text)
                    print("find id is ok")
                    name = (tds[2].text)
                    print("find name is ok")
                    mod = (tds[3].text)
                    print("find mod is ok")
                    # useCount = (tds[4].text)
                    print(f"get data is {name}")
                    lsData.append({"this row" : rw,
                        report_output_cols.id : id,  report_output_cols.name : name,
                        report_output_cols.mod : mod, report_output_cols.useCount : 0 })
                print("data download ok")
                
                if counter >= 20:
                    counter = 0
                    data = pd.DataFrame(lsData)
                    data.to_excel(f"{title}.xlsx",index=False)
                print("load")
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                print("scrool")
                time.sleep(0.5)
                element =driver.find_element(By.XPATH,xph.create_coin_report_hesabro.next_p)
                # time.sleep(3)
                
                
                if element.is_displayed():
                        element.click()
                        time.sleep(3)
                else:
                    is_true = True
                    # driver.close()
                # time.sleep(6)
            except Exception as e:
                currAdderss = driver.current_url
                driver.get(currAdderss)
                time.sleep(4)
                data = pd.DataFrame(lsData)
                data.to_excel(f"{title}.xlsx",index=False)
                # is_true = True
            
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

            
def get_coin_report_data(driver, title, this_address, **kwargs): 
    #  1- تغییر آدرس مرورگر به صفححه ایجاد گزاشات
    # this_address = app_address.urls["birthday"]["create_rpt"]
    # this_address = app_address.url_address.create_report.birthday
    driver.get(this_address)
    time.sleep(3)
    # print(driver.get(this_address))
    print("check address")
    this_delay = 3
    while driver.current_url != this_address: # جهت اطمینان از باز شدن صفحه ی درخواست شده در گزینه 1 از حلقه استفاده شده است
        driver.get(this_address)
        time.sleep(this_delay)
        this_delay += 1
    
    # this_delay 
    
    print("address is loaded")

    this_delay = 3
    
    dfData = download_data(driver, title, this_delay)
    return dfData




    # is_true = False
    # while is_true==False:
    #     try:
    #         element = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, xph.create_reportcustomer.download)))
    #         this_file_path=element.get_attribute("href")
    #         # print(this_file_path)
    #         url = this_file_path
    #         this_file = requests.get(url, allow_redirects=True)
    #         # print(this_file)
    #         # this_file = requests.get(this_file_path)
    #         this_path = os.getcwd()
    #         # print(this_path)
    #         open(f"{this_path}/{title}.xls", "wb").write(this_file.content)
    #         #     f.write(this_file.content)
    #         #     f.close()
    #         # # write_in_element(birthdaytoday, element)
    #         is_true = True
    #     except:
    #         is_true = False
