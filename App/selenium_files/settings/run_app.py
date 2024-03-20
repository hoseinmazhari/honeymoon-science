
from . import printProgress as prgs
import os,sys
from .browser import Browser,write_in_element
from selenium.webdriver.common.keys import Keys
import time
from .xpath import get_xpath
import pandas as pd
# import app_address
from .app_address import hesabro_domain,get_rnd_page,urls,arad_payamek_domain,honeymoonatr_domain
import random
from . import DateJuToJa as djtj
from .user_pass import get_index_user_pass
from . import xpath
from . import app_address
from ..hesabro.merchandise.order_points import set_order_point
from ..hesabro.merchandise.order_points_allBrs import set_order_point_allBrs
from . import app_tasks as tsk
from ..hesabro.club import fetch_birthday as upb
from ..hesabro.club import fetch_report_data as frd
from ..hesabro.club import fetch_coin_report_data as fcrd
from ..hesabro.club.sms_sender import send_group_sms
from ..honeymoonatr import update_products as upsh
def get_user_pass(this_domain):
    df_user_pass = pd.read_excel("..//selenium_files/data/user_pass/user_pass.xlsx")
    df_user_pass.to_excel("test.xlsx", index=False)
    df_data = df_user_pass.loc[df_user_pass['domain']==this_domain]
    # if len(df_hesabro)
    this_index = get_index_user_pass(df_data)
    # for i in range(1000):
    #     print(this_index.have_username)
    have_username = df_data.iat[0,this_index.have_username]
    if have_username == "True" or have_username == True:
        username = df_data.iat[0,this_index.username]
    else:
        username = ""
    have_password = df_data.iat[0, this_index.have_password]
    if have_password == "True" or have_password== True:
        password = df_data.iat[0,this_index.password]
    else:
        password = ""
    return username,password

def run_arad_payamek(driver):
    driver.get(arad_payamek_domain)
    username,password = get_user_pass(arad_payamek_domain)
    print(username)
    time.sleep(5)
    element = driver.find_element(by="xpath",value=xpath.aradpayamak.login_page.username)
    element.click()
    write_in_element(username,element)
    element = driver.find_element(by="xpath",value=xpath.aradpayamak.login_page.password)
    element.click()
    write_in_element(password,element)
    element = driver.find_element(by="xpath",value=xpath.aradpayamak.login_page.btn_login)
    element.click()
    # element.send_keys(Keys.ENTER)
    driver.get(app_address.urls_arad.simple_send_sms.send_page)

    time.sleep(5)
    return driver
def arad_send_simple_sms(driver,sms_text,number):
    element = driver.find_element(by = "xpath", value=xpath.aradpayamak.simple_send_sms.input_sms )
    element.click()
    element.clear()
    write_in_element(sms_text,element)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    element = driver.find_element(by = "xpath", value=xpath.aradpayamak.simple_send_sms.input_number)
    element.click()
    element.clear()
    write_in_element(number,element)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    element = driver.find_element(by = "xpath", value=xpath.aradpayamak.simple_send_sms.btn_send )
    element.click()
    time.sleep(3)
    return driver
def run_hesabro():
    # sys.path.append("..")
    # for i in range(1000):
        # print(os.getcwd())
        # print(app_tasks.tasks.update_birthday)
    
    main_url= f"{hesabro_domain}/site/index"
    username,password = get_user_pass(hesabro_domain)
    thisTime = djtj.getDateTimeForFileName()

    is_logged_in = False
    mybrowser = Browser()
    mybrowser.change_url(main_url)
    driver = mybrowser.driver
    # number = driver.find_element(by="id",value='loginform-number')
    files = os.listdir()
    file_exist = False
    cookies_file_name = f'cookies_hesabro_{username}'
    for f in files:
        # print(f)
        if f'{cookies_file_name}.pkl'== f:
            file_exist = True
            break
    # logged_in = True
    if file_exist:
        mybrowser.rem_cookies()
        mybrowser.load_cookies(f'{cookies_file_name}')
        time.sleep(4)
        if mybrowser.driver.current_url == main_url:
            is_logged_in = True
        else:
            driver.get(main_url)
            os.remove(f'{cookies_file_name}.pkl') 
            time.sleep(5)
                
    if is_logged_in == False:
        # login_hesabro(driver)
        driver.get(main_url)
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
            Browser.save_cookies(mybrowser,cookies_file_name)
            is_logged_in = True
        
        except:
            is_logged_in = False
    return driver , is_logged_in

def run_honeymoonatr():
    print("now set data to variables")
    print_delay = .4
    time.sleep(print_delay)
    main_url= f"{honeymoonatr_domain}" 
    cookie_fileName = "honeymoonatr_cookies"
    time.sleep(print_delay)
    cookies_path = app_address.file_locations.cookies
    print("set data to variables is complete!")
    time.sleep(print_delay)
    print("start run mozilla bot")
    time.sleep(print_delay)
    mybrowser = Browser()
    driver = mybrowser.driver
    print(f"start load site {honeymoonatr_domain}")
    time.sleep(print_delay)
    driver.get(main_url)
    print(f"site {honeymoonatr_domain} is now loaded!")
    time.sleep(print_delay)
    print(f"now we start check existing saved cookies")
    time.sleep(print_delay)
    thisPath = os.getcwd()
    os.chdir(f"{thisPath}/{cookies_path}")
    print("change url to cookies path")
    time.sleep(print_delay)
    ls_files = os.listdir()
    print("change app url is performed")
    time.sleep(print_delay)
    print(f"check cookie file for {honeymoonatr_domain} ")
    time.sleep(print_delay)
    print("file list is:")
    time.sleep(print_delay)
    is_logged_in = False
    for f in ls_files:
        # print(f)
        # time.sleep(print_delay)
        if f == f"{cookie_fileName}.pkl":
            print(f"cookie for {honeymoonatr_domain} is now avalible!")
            time.sleep(print_delay)
            
            print("first remove cookeis in browser")
            time.sleep(print_delay)
            mybrowser.rem_cookies()
            print("remove cookeis on browser is completed")
            time.sleep(print_delay)
            print("now start loading cookie to your browser")
            time.sleep(print_delay)
            for i in range(10, -1):
                print(i, end="\r")
                time.sleep(print_delay)
            
            mybrowser.load_cookies(f'{cookie_fileName}')
            
            print(f"cookie file for {honeymoonatr_domain} is successfully loaded!")
            time.sleep(print_delay)
            print("now exit check cookies files")
            time.sleep(print_delay)
            is_logged_in = True
            break
    return driver, is_logged_in 
    # time.sleep(20)
    
    
    # for i in range(1, 6):
    #     print(i, end="\r")
    #     time.sleep(1)
    
        
    #/di-admin"
    # username,password = get_user_pass(honeymoonatr_domain)
    # thisTime = djtj.getDateTimeForFileName()

    # is_logged_in = False
    
    # mybrowser.change_url(main_url)
    
    # print("load main_url")
    # driver.get(main_url)
    return False
    for i in range(30):
            print(i, end="\r")
            time.sleep(1)
    # print("load main_url is complete0")
    
    waiter = input("press any key and enter: ")
    is_true = False
    while is_true ==False:
        try:
            Browser.save_cookies(mybrowser,"honeymoonatr_cookies")
            time.sleep(3)
            is_true =True
        except:
            pass
    print("cookies is saved please wait...")
    for i in range(30):
            print(i, end="\r")
            time.sleep(1)
    driver.get("https://honeymoonatr.com/wp-admin/edit.php?post_type=product")
    
    
    
    
    return True
    # number = driver.find_element(by="id",value='loginform-number')
    # thisPath = os.getcwd()
    # os.chdir(f"{thisPath}/cookies")
    # files = os.listdir()
    # print(files)
    # print(os.getcwd())
    # # file_exist = False
    # cookies_file_name = f'cookies'
    # cookie = {"name": "PHPSESSID", 
    #            "value":"e20a5d206e0f148c0e8936fa5665898b"}
    # driver.add_cookie(cookie)
    # for f in files:
    #     # print(f)
    #     if f'{cookies_file_name}.pkl'== f:
    #         file_exist = True
    #         break
    # # logged_in = True
    # if file_exist:
    # if True:
        # mybrowser.rem_cookies()
        # print("start load cookies")
        # mybrowser.load_cookies(f'{cookies_file_name}')
        
        # # time.sleep(120)
        # if mybrowser.driver.current_url == main_url:
        #     is_logged_in = True
        # else:
            # driver.get(main_url)
            # os.remove(f'{cookies_file_name}.pkl') 
            # time.sleep(5)
    return False        
    if is_logged_in == False:
        # login_hesabro(driver)
        driver.get(main_url)
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
            Browser.save_cookies(mybrowser,cookies_file_name)
            is_logged_in = True
        except:
            is_logged_in = False
    return driver , is_logged_in


def task_selector(selected,args_= "",**kwargs):
        # print("type:")
        # print("1 : for charge setter!")
        # print(f"2 : matrook nemoodan list kala ")
        # print("3: de matrook list kala")
        # print("4: update sale and buy price for testers")
        # print("5: set noghte sefaresh")
        # selected = input("please type and then enter num of your choice: ")
        # selected = "5"
        main_url = f"{hesabro_domain}/site/index"
        print(selected)
        if selected == tsk.task_name.run_honeymoonatr:
            # print("seledted is ok")
            driver, is_logged_in =run_honeymoonatr()
            if is_logged_in:
                
                upsh.start_update(driver)
                
        elif selected == tsk.task_name.update_birthday:
            driver, is_logged_in = run_hesabro()
            if is_logged_in:
                dfData = upb.get_birthday_data(driver,main_url,tsk.task_name.update_birthday)
                send_group_sms(dfData,tsk.task_name.update_birthday,args_)
                try:
                    birthPath = os.getcwd()
                    reports = "reports"
                    os.mkdir(reports)
                except:
                    pass
                os.chdir(f"{birthPath}/{reports}")
                birthPath = os.getcwd()
                try:
                    birthdayDir = "birthday"
                    os.mkdir(birthdayDir)
                except:
                    pass
                os.chdir(f"{birthPath}/{birthdayDir}")
                dfData.to_excel(f"birthday in {djtj.getDateTimeForFileName()}.xlsx",index=False)
            # mybrowser = Browser()
            # # mybrowser.change_url(main_url)
            # driver = mybrowser.driver
            # driver = run_arad_payamek(driver)
            # sms_text = "تست ارسال پیامک\nلغو 11"
            # number = '09162078094'

            
            # msg = "#نام و نام خانوادگی عزیز سلام\nتولدت مبارک\n20% تخفیف نقدی تا 10 روز برای شما در تمامی شعب هانی مون"
            # _msg = args_
            # args_ = "test\n لغو 11"
            mobile = "موبایل"
            name = "نام و نام خانوادگی"
            birthday = "تاریخ تولد"
            ls = []
            # this_dict = {
            #     mobile:"09136199868",
            #     name: "علی خراسانی",
            #     birthday:"1380/01/01"}
            # ls.append(this_dict)
            # this_dict = 
            ls.append({mobile:"09139960164", name: "حسین مظهری", birthday:"1365/06/29"})
            dfData = pd.DataFrame(ls)
            dfData.to_excel("data.xlsx",index=False)
            send_group_sms(dfData,tsk.task_name.update_birthday,args_)
            # time.sleep(60)
            # driver.close()
        elif selected == tsk.task_name.get_report_from_hesabro_link:
            driver, is_logged_in = run_hesabro()
            print("this select")
            if is_logged_in:
                dfData = frd.get_report_data(driver,tsk.task_name.get_report_from_hesabro_link,args_)
            dfData.to_excel("report_data.xlsx",index=False)
        elif selected == tsk.task_name.get_coin_report_from_hesabro_link:
            driver, is_logged_in = run_hesabro()
            print("hesabro is running")
            if is_logged_in:
                print("run download")
                dfData = fcrd.get_coin_report_data(driver,tsk.task_name.get_coin_report_from_hesabro_link,args_)
            # dfData.to_excel("report_data.xlsx",index=False)
        elif selected == tsk.task_name.set_order_point:
            driver,is_logged_in = run_hesabro()

            # driver = "1"
            # is_logged_in = True
            if is_logged_in:
                set_order_point_allBrs(driver,main_url)
        elif selected == "1":
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
            