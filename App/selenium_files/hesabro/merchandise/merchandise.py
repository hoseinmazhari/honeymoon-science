from ...settings.xpath import get_xpath
from ...settings.app_address import get_address
from ...settings.browser import Browser,write_in_element
from selenium.webdriver.common.keys import Keys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def check_matrook(driver,main_url):
    is_matrook = True
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','list')}")))
        element.click()
    except:
        return False
    time.sleep(5)
    element = driver.find_element(by="xpath",value=f"{get_xpath('merchandise','search_btn')}")
    # try:
    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','search_btn')}")))
    element.click()
    # element = driver.find_element(by="xpath",value=f"{get_xpath('merchandise','matrook')}")
    
    
    # except Exception as e:
    #     print(e)
    #     return False
    try:
        abandoned = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','productsearch-abandoned')}")))
        abandoned.send_keys(Keys.SPACE)
    except:
        # print("abandoned is ok")
        return False
    is_sh_name = False
    while is_sh_name == False:
        try:
            time.sleep(2)
            driver.execute_script("return arguments[0].scrollIntoView();", element)

            element = driver.find_element(by="xpath",value=f"{get_xpath('merchandise','productsearch_sh_name')}")
            # element = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','productsearch_sh_name')}")))
            element.click()
            time.sleep(2)
            # print("sh_name is ok")
            is_sh_name = True
            element.send_keys(Keys.ENTER)
        except:
            
            is_sh_name = False
        
    try:

        time.sleep(5)
        element = driver.find_element(by="xpath",value=f"{get_xpath('merchandise','table')}")
        driver.execute_script("return arguments[0].scrollIntoView();", element)
        # abandoned
        time.sleep(2)
        elements = driver.find_elements(by="xpath",value=f"{get_xpath('merchandise','btn')}")
        element = elements[0]

        # # element = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','btn')}")))
        element.click()
    except:
        return False
    # try:
    time.sleep(2)
        # _menu = driver.switch_to.active_element
        # time.sleep(2)

    # driver.execute_script('document.getElementById("stateSelect").selectedIndex = 1;')
    elements = driver.find_elements(by="xpath",value=f"{get_xpath('merchandise','menu_items')}")
    element = elements[1]

        # elements = _menu.find_element(by="xpath",value=f"{get_xpath('merchandise','update_btn')}")
        # element = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','update_btn')}")))
    element.click()
    # except:
    #     return False
    try:
        time.sleep(2)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','check_exit')}")))
        element.send_keys(Keys.SPACE)
        time.sleep(1.5)
    except:
        return False
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','btn_submit')}")))
        element.click()
    except:
        return False

    return is_matrook
def search_fieldProduct(driver):
    is_search_fieldProduct =False
    while is_search_fieldProduct == False:
        try:
            _search = driver.find_element(by="xpath",value=f"{get_xpath('search','merchandise')}")
            #driver.execute_script("return arguments[0].scrollIntoView();", _search)
            _search.click()
            is_search_fieldProduct = True
            time.sleep(1)
        except:
            pass
    return is_search_fieldProduct

def update_product(act,merchandise,driver,main_url):
    if act== "exit_product":
        is_search_fieldProduct = search_fieldProduct(driver)
        # while search_fieldProduct(driver)
        _product_input = driver.switch_to.active_element
        
        write_in_element(merchandise,_product_input)
        _product_input.send_keys(Keys.ENTER)
        time.sleep(3.5)
        
        _product_input.send_keys(Keys.ENTER)
        time.sleep(3.5)
        driver.implicitly_wait(2)
        while driver.current_url!=main_url:
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','act_button')}")))
                element.click()
            except:
                pass
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','update_btn')}")))
                element.click()
            except:
                pass
            try:
                time.sleep(2)
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','check_exit')}")))
                element.send_keys(Keys.SPACE)
                time.sleep(1)
            except Exception as e:
                print(e)
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{get_xpath('merchandise','btn_submit')}")))
                element.click()
                while driver.current_url!= main_url:
                    driver.get(main_url)
                    time.sleep(2)
            except:
                pass
            is_search_fieldProduct = search_fieldProduct(driver)
            _product_input = driver.switch_to.active_element
        
            write_in_element(merchandise,_product_input)
            _product_input.send_keys(Keys.ENTER)
            time.sleep(3.5)
            
            _product_input.send_keys(Keys.ENTER)
            time.sleep(3.5)
            driver.implicitly_wait(2)
 
  






def sum_product(this_url,driver,main_url):
    print(this_url)




