import requests
from ...settings import xpath_hesabro as xph
from ...settings import DateJuToJa as djtj
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from .xpath import get_xpath
from ....settings.xpath import get_xpath
import time
import pandas as pd
import os
from selenium.webdriver.common.keys import Keys
# from .merchandise import search_fieldProduct
from ....settings.browser import write_in_element
from ...settings import app_address
from tqdm import tqdm
import urllib.request
import shutil

# url = "http://www.somewebsite.com/something.pdf"

def dwn(driver):
    addd= "https://hesabro.ir/@hm/report-customer/view?id=59"
    driver.get(addd)
    time.sleep(2)
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
                    birthday=(tds[4].text)
                    mobile=(tds[7].text)
                    lsData.append({"mobile":mobile, "name":name, "birthday":birthday})
                    data = pd.DataFrame(lsData)
                    data.to_excel("new way to birthdays.xlsx",index=False)
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(1.2)
                element =driver.find_element(By.XPATH,xph.create_reportcustomer.dataReport.next_p)
                if element.is_enabled():
                        element.click()
                        time.sleep(3)
                else:
                    is_true = True
                    driver.close()
                # time.sleep(6)
            except Exception as e:
                print(e)
                is_true = True
            #     time.sleep(5)
            #     is_true = False
        data = pd.DataFrame(lsData)
        data.to_excel("new way to birthdays.xlsx",index=False)
            # element = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, xph.create_reportcustomer.download)))
    except Exception as e:
        print(e)
        is_true = False
            
            # a = 0
            
            # this_file_path=element.get_attribute("href")
            # print(this_file_path)
            # url = this_file_path
            # output_file = "save_this_name.xls"
            # with urllib.request.urlopen(url) as response, open(output_file, 'wb') as out_file:
            #     shutil.copyfileobj(response, out_file)
            # this_file = requests.get(url, allow_redirects=True)
            # print(this_file)
            # this_file = requests.get(this_file_path)
            # this_path = os.getcwd()
            # # print(this_path)
            # for i in range(100):
            #       print(this_file.content)
            # with  open('facebook.xls', 'wb') as f:
            # # open(f"test.xls", "wb").write(this_file.content)
            #     f.write(this_file.content)
            #     f.close()
            # # write_in_element(birthdaytoday, element)
    #         is_true = True
    # except:
    #         is_true = False
