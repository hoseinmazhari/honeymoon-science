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
from .merchandise import search_fieldProduct
from ...settings.browser import write_in_element
from ...settings import xpath


	 			 	# بارکد	موجودی تمام انبار	ایجاد شده
class ThisCols():
    id = 'آیدی'
    category = 'دسته بندی'
    brand = 'برند'
    store_price = 'قیمت فروشگاه'
    site_price = 'قیمت سایت'
    site_active = 'فعال بودن در سایت'
    buy_price = 'قیمت روز خرید'
    order_point = 'کف سفارش'
    Supplier = "تامین کننده"

def get_index_products_cols(df):
    thisItter = -1
    thisClass = ThisCols()
    for col in df.columns:
        thisItter += 1
        if col == thisClass.id:
            thisClass.id = thisItter # type: ignore
        elif col == thisClass.category:
            thisClass.category = thisItter
        elif col == thisClass.buy_price:
            thisClass.buy_price = thisItter # type: ignore
        elif col == thisClass.brand:
            thisClass.brand = thisItter # type: ignore
        elif col == thisClass.order_point:
            thisClass.order_point = thisItter # type: ignore
        elif col == thisClass.site_price:
            thisClass.site_price = thisItter # type: ignore
        elif col == thisClass.site_active:
            thisClass.site_active = thisItter # type: ignore
        elif col == thisClass.Supplier:
            thisClass.Supplier = thisItter # type: ignore
    return thisClass
       
def _products_update(driver,main_url,id,order_point): 
    # if act== "exit_product":
        is_true = True
        is_search_fieldProduct = search_fieldProduct(driver)
        # while search_fieldProduct(driver)
        _product_input = driver.switch_to.active_element
        
        write_in_element(id,_product_input)
        _product_input.send_keys(Keys.ENTER)
        time.sleep(3.5)
        
        _product_input.send_keys(Keys.ENTER)
        time.sleep(3.5)
        driver.implicitly_wait(2)
        # while driver.current_url!=main_url:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','act_button')}")))
            element.click()
        except:
            is_true = False
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','update_btn')}")))
            element.click()
        except:
            is_true = False
        try:
            time.sleep(2)
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath.hesabro.merchandise))
            element.click()
            # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1)
            element = driver.find_element(By.TAG_NAME,"html")
            for i in range(12):
                time.sleep(0.4)
                element.send_keys(Keys.DOWN)
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','order_point')}")))
            element.click()
            for i in range(20):
                time.sleep(0.04)
                element.send_keys(Keys.BACKSPACE)
            time.sleep(1)
            for i in range(20):
                time.sleep(0.04)
                element.send_keys(Keys.DELETE)
            time.sleep(1)
            element.clear()
            write_in_element(order_point,element)
            
            time.sleep(1)
        except Exception as e:
            print(e)
            is_true = False
        
       
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','btn_submit')}")))
            element.click()
            time.sleep(2)
            while driver.current_url!= main_url:
                driver.get(main_url)
                time.sleep(2)
        except:
            is_true = False
        return is_true
        # is_search_fieldProduct = search_fieldProduct(driver)
        # _product_input = driver.switch_to.active_element
    
        # write_in_element(merchandise,_product_input)
        # _product_input.send_keys(Keys.ENTER)
        # time.sleep(3.5)
        
        # _product_input.send_keys(Keys.ENTER)
        # time.sleep(3.5)
        # driver.implicitly_wait(2)
    
def set_update_products_data(driver,main_url):
    print("please wait until see 'done'...")
    thisPath = os.getcwd()
    todayIs = djtj.getDateTimeForFileName()
    counter = 0
    dfData = pd.read_excel("..//dist/order point/products.xlsx")
    thisIndex = get_index_products_cols(dfData)
    ls_true = []
    ls_false = []
    while len(dfData):  
        counter += 1
        merchandise = dfData.iat[0,thisIndex.name]
        order_point = f"{int(dfData.iat[0,thisIndex.order_point])}"
        
        id = f"{int(dfData.iat[0,thisIndex.id])}"
        
        # print(counter)

        is_True = _products_update(driver,main_url,id,order_point)
        if is_True:
            dfData = dfData.loc[dfData[ThisCols.id]!= int(id)]

            # dfData.to_excel(f"ثبت نشده های بروزرسانی محصولات.xlsx",index= False)
        else:
            import random as r
            sl = r.randint(20,80)
            print(f"please wait for {sl} seconds ...")
            time.sleep(sl)
            driver.get(main_url)
            time.sleep(5)