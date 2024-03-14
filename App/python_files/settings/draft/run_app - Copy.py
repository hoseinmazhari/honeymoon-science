from testers.testers_defs import testersPrice
from merchandises.details_defs import set_order_point
from merchandises.deactive_products import deactive_product
from merchandises.create_products import create_product
from merchandises.price_changer import price_changer
from merchandises.create_testers import create_testers
import printProgress as prgs
import os
from browser import Browser,write_in_element
from selenium.webdriver.common.keys import Keys
import time
from xpath import get_xpath
import pandas as pd
# import app_address
from app_address import this_domain,get_rnd_page,urls
import random
from coin import coin_setter
from merchandise import update_product,check_matrook
# from bidi import *
# from arabic_reshaper import *
import bidi
import arabic_reshaper
# from product import sum_product
# from goto import goto,lable
username= "09139960164"
password ="91001055"
# f = open("username.txt","r")
# for line in f.readlines():
#     print(line)
# f.close()
# for l in list_:
    # print(l)
# this_domain = "https://hm.hesabro.ir"
main_url= f"{this_domain}/site/index"
import DateJuToJa as djtj
thisTime = djtj.getDateTimeForFileName()

def main():
    is_logged_in = False
    mybrowser = Browser()
    mybrowser.change_url(main_url)
    driver = mybrowser.driver
    # number = driver.find_element(by="id",value='loginform-number')
    files = os.listdir()
    file_exist = False
    for f in files:
        # print(f)
        if f'{username}.pkl'== f:
            file_exist = True
            break
    # logged_in = True
    if file_exist:
        mybrowser.rem_cookies()
        mybrowser.load_cookies(f'{username}')
        time.sleep(4)
        if mybrowser.driver.current_url == main_url:
            is_logged_in = True
               
    if is_logged_in == False:
        # login_hesabro(driver)
        _number = driver.find_element(by="xpath",value=f"{get_xpath('login','number')}")
        
        write_in_element(username,_number)
        _number.send_keys(Keys.ENTER)

        _password = driver.find_element(by="xpath",value=f"{get_xpath('login','password')}")
        write_in_element(password,_password)
        
        _authenticator = driver.find_element(by="xpath",value=get_xpath('login','authenticator'))
        _authenticator.click()
        time.sleep(15)
        _authenticator.send_keys(Keys.ENTER)
        time.sleep(7)
        try:
            # _test = _coin = driver.find_element(by="xpath",value=get_xpath('user_detail','coin'))
            print('this message show for wait to logged in after login continue')
            waiter = input("press any key and enter: ")
            Browser.save_cookies(mybrowser,username)
            is_logged_in = True
        except:
            is_logged_in = False
    if is_logged_in:

        print("type:")
        print("1 : for charge setter!")
        print(f"2 : matrook nemoodan list kala ")
        print("3: de matrook list kala")
        print("4: update sale and buy price for testers")
        print("5: set noghte sefaresh")
        # selected = input("please type and then enter num of your choice: ")
        selected = "5"
        if selected == "1":
            print("charges is loading! plese wait...")
            dfData = pd.read_excel('newCharge.xlsx')
            print('charge file now upload successfully')
            _ls_deactive_users = []
            _ls_active_users = []
            l = len(dfData)
            print(f'numer of mobiles is {l}')
            
            save_counter = 0
            while len(dfData):
                save_counter += 1
                driver.get(main_url)
                time.sleep(2.5)
                mobile = dfData.iat[0,0]
                user = dfData.iat[0,1]
                this_mobile = f"0{int(mobile)}"
                coin = str(dfData.iat[0,2])
                prgsCounter = l- len(dfData)
                prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 25)    
                # print(f"charge {mobile} is doing! please wait...")
                hamyar_condition = True
                # if prgsCounter > 10:
                #     hamyar_condition =False
                action_True = coin_setter(this_mobile,driver,main_url,coin,hamyar_condition)
                
                dfData = dfData.loc[dfData["mobile"]!=mobile]
                if action_True==False:
                    # file.writelines(this_mobile)
                    _ls_deactive_users.append({'mobile':this_mobile,'user':user,"coin":coin})
                    
                    # false_count += 1
                else:
                    
                    _ls_active_users.append({'mobile':this_mobile,'user':user,"coin":coin})
            
                item = random.randint(1,len(urls['random']))
                rnd_page = get_rnd_page(item)
                driver.get(rnd_page)
                time.sleep(1)
                while driver.current_url != rnd_page:
                    driver.get(rnd_page)
                    time.sleep(3)
                if save_counter>10:
                    save_counter = 0
                    dfData.to_excel("newCharge.xlsx",index=False)
                time.sleep(random.randint(3,6))
                
                thisPath = os.getcwd()
                acdcu = "active and deactive users"
                try:
                    os.mkdir(acdcu)
                except:
                    pass
                os.chdir(acdcu)
                if len(_ls_active_users):
                    df_active_users = pd.DataFrame(_ls_active_users)
                    try:
                        df_active_users.to_excel(f"active users{thisTime}.xlsx",index=False)
                    except:
                        pass
                if len(_ls_deactive_users):
                    df_deactive_users = pd.DataFrame(_ls_deactive_users)
                    try:
                        df_deactive_users.to_excel(f'deactive users{thisTime}.xlsx',index=False)
                    except:
                        pass
                os.chdir(thisPath)
                # if len(_ls_active_users):
                #     df_active_users = pd.DataFrame(_ls_active_users)
                #     try:
                #         df_active_users.to_excel(f"active users.xlsx",index=False)
                #     except:
                #         pass
                # if len(_ls_deactive_users):
                #     df_deactive_users = pd.DataFrame(_ls_deactive_users)
                #     try:
                #         df_deactive_users.to_excel('deactive users.xlsx',index=False)
                #     except:
                #         pass
        elif selected == "2"        :
            dfData = pd.read_excel("product.xlsx")
            print('product file now upload successfully')
            _ls_deactive_users = []
            _ls_active_users = []
            l = len(dfData)
            print(f'numer of product is {l}')
            
            save_counter = 0
            while len(dfData):
                save_counter += 1
                driver.get(main_url)
                time.sleep(2.5)
                merchandise = dfData.iat[0,0]
                # user = dfData.iat[0,1]
                # this_mobile = f"0{int(mobile)}"
                # coin = str(dfData.iat[0,2])
                prgsCounter = l- len(dfData)
                prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 25)    
                # print(f"charge {mobile} is doing! please wait...")
                # hamyar_condition = True
                # if prgsCounter > 10:
                #     hamyar_condition =False
                # from product import update_product
                act = "exit_product"
                action_True = update_product(act,merchandise,driver,main_url)
                
                dfData = dfData.loc[dfData["merchandise"]!=merchandise]
                
        elif selected == "3":
            print("please wait until see 'done'...")
            matrook = True
            counter = 0
            while matrook:
                counter += 1
                print(counter)
                matrook = check_matrook(driver,main_url)

            print("done")
        elif selected == "4":
            testersPrice(driver,main_url)

            print("done")
        elif selected == "5":
            set_order_point(driver,main_url)
        elif selected == "6":
            create_product_address = urls["product"]["create_product"]
            create_product(driver,main_url,create_product_address)
        elif selected == "7":
            deactive_product(driver,main_url)
        elif selected == "8":
            price_changer(driver,main_url)
        elif selected == "9":
            create_product_address = urls["product"]["create_product"]
            create_testers(driver,main_url,create_product_address)
            # dfData = pd.read_excel("product.xlsx")
            # print('product file now upload successfully')
            # _ls_deactive_users = []
            # _ls_active_users = []
            # l = len(dfData)
            # print(f'numer of product is {l}')
            
            # save_counter = 0
            # while len(dfData):
            #     save_counter += 1
            #     driver.get(main_url)
            #     time.sleep(2.5)
            #     merchandise = dfData.iat[0,0]
            #     # user = dfData.iat[0,1]
            #     # this_mobile = f"0{int(mobile)}"
            #     # coin = str(dfData.iat[0,2])
            #     prgsCounter = l- len(dfData)
            #     prgs.printProgressBar(prgsCounter, l, prefix = 'Progress:', suffix = 'Complete', length = 25)    
            #     # print(f"charge {mobile} is doing! please wait...")
            #     # hamyar_condition = True
            #     # if prgsCounter > 10:
            #     #     hamyar_condition =False
            #     # from product import update_product
            #     act = "exit_product"
            #     action_True = update_product(act,merchandise,driver,main_url)
                
            #     dfData = dfData.loc[dfData["merchandise"]!=merchandise]
        
if __name__ == '__main__':
    main()            