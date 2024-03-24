from ..settings import xpath_honeymoonatr as xph
from ..settings import DateJuToJa as djtj
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from .xpath import get_xpath
# from ...settings.xpath import get_xpath
import time
import pandas as pd
import os

from selenium.webdriver.common.keys import Keys
# from .merchandise import search_fieldProduct
# from ...settings.browser import write_in_element
from ..settings import app_address
# from tqdm import tqdm
# from .te

# from ..browser import Browser,write_in_element
def page_progress(driver):
    element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xph.all_products.tbl)))
    
    element = WebDriverWait(element, 10).until(
                EC.presence_of_element_located((By.XPATH, xph.all_products.tbody)))
    
    trs = element.find_elements(By.TAG_NAME, "tr")
    ls_page = []
    for tr_index in trs:
        is_find = False
        this_id =  tr_index.get_attribute("id")
        dashIndex = this_id.find("-")+1
        this_id = this_id[dashIndex:]
        # print(this_id)
        this_address = (f"{app_address.urls_honeymoonatr.products.step_one_product}{this_id}{app_address.urls_honeymoonatr.products.step_tow_product}")
        print(this_address)
    
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)
        driver.get(this_address)
        time.sleep(5)
        element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xph.product_details.name)))
        
        input_text = element.get_attribute("value")
        ls_page.append({"id":this_id, "name":input_text})
        # df= pd.DataFrame(ls_page)
        # df.to_excel("step1.xlsx",index=False)
        # element = WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, xph.product_details.update)))
        
        # element.click()
        # time.sleep(8)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)
    return pd.DataFrame(ls_page)
def next_page(driver, page_number):
    # is_true = True
    
    # while is_true:
        
        try:
            # element = driver.find_element(By.XPATH,xph.all_products.next_p)
            # element = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, xph.all_products.next_p)))
            # element.click()
            is_true = True
            page_number += 1
            this_url = f"{app_address.urls_honeymoonatr.products.next_page}{page_number}"
            driver.get(this_url)
            time.sleep(5)
            if driver.current_url != this_url:
                is_true = False
                for i in range(10):
                    print("complete and is_true set false")
        except:
            for i in range(10):
                print("is true set false")
            is_true = False
            # time.sleep(2)
        return is_true, page_number
def start_update(driver):
    # mybrowser = Browser()
    # driver = mybrowser.driver
    thisPath = os.getcwd()
    all_products = app_address.urls_honeymoonatr.products.all_products
    driver.get(all_products)
    time.sleep(3)
    element = driver.find_element(By.XPATH,xph.all_products.published)
    element.click()
    time.sleep(4)
    ls_data = []
    ls_data.append(page_progress(driver))
    page_number = 1
    next_p_isTrue, page_number = next_page(driver,page_number)
    while (next_p_isTrue):
        print(os.getcwd())
        ls_data.append(page_progress(driver))
        next_p_isTrue, page_number = next_page(driver,page_number)
        # df = pd.DataFrame(ls_data)
        # print(os.getcwd())
        # df.to_excel("products.xlsx",index= False)
    df = pd.concat(ls_data)
    df.to_excel("finalProductInHoneymoonatr.xlsx", index = False)
    driver.close()
    # body = driver.find_element(By.XPATH,'//*[@id="wpbody-content"]')
    # for i in range(3):
    #     body.send_keys(Keys.DOWN) 
    #     time.sleep(.4)
    # # return False
   