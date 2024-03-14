from . import printProgress as prgs
import os,sys
# from .browser import Browser,write_in_element
from selenium.webdriver.common.keys import Keys
import time
from .xpath import get_xpath
import pandas as pd
# import app_address
from .app_address import hesabro_domain,get_rnd_page,urls,arad_payamek_domain
import random
from . import DateJuToJa as djtj
from .user_pass import get_index_user_pass
from ..codes.a00001_invoices import a0_1_invoices_Count as isc
# from ..hesabro.merchandise.order_points import set_order_point
# from ..hesabro.merchandise.order_points_allBrs import set_order_point_allBrs
from . import app_tasks as tsk
# from ..hesabro.club import fetch_birthday as upb
# from ..hesabro.club import fetch_report_data as frd
# from ..hesabro.club.sms_sender import send_group_sms
def get_user_pass(this_domain):
    df_user_pass = pd.read_excel("..//selenium_files/data/user_pass/user_pass.xlsx")
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
# from . import xpath
# from . import app_address


def task_selector(selected,args_= "",**kwargs):
        
        if selected == tsk.task_name.invoices_count:
            pass
            # driver.close()
       