import requests
import pandas as pd
import time
from .fetch_birthday import birthday_output_cols as boc_class
from ...settings.app_tasks import task_name 
def get_index_boc(df):
    this_itter = -1
    this_class = boc_class()
    for col in df.columns:
        this_itter += 1
        if col == this_class.birthday:
           
            this_class.birthday = this_itter
        elif col == this_class.mobile:
            this_class.mobile = this_itter
        elif col == this_class.name:
            this_class.name = this_itter
    return this_class

# URL و پارامترهای مربوط به ارسال پیامک
url = "http://aradpayamak.net/APPs/SMS/postsms/send.php"
def send_sms(domain_ = 'http://aradpayamak.net', username_ = 'hanimoon', password_ = '1339754', 
             from_ = '10008546', to_ = '09162078094', text_ = 'تست', isflash = 0):
    params = {
        'domain': domain_,        # دامنه
        'username': username_,    # نام کاربری
        'password': password_,    # رمز عبور
        'from': from_,        # شماره فرستنده
        'to': to_,        # شماره گیرنده (می‌توانید چند شماره را با ویرگول جدا کنید)
        'text': f'{text_}\n لغو 11',    # متن پیام
        'isflash': isflash                    # اگر می‌خواهید پیامک فلش (isflash) باشد، مقدار 1 را تنظیم کنید
    }

    # ارسال درخواست POST به وب سرویس
    response = requests.post(url, params=params)

    # بررسی کد وضعیت HTTP
    if response.status_code == 200:
        # تجزیه و تحلیل پاسخ JSON (اگر وب سرویس JSON بازگشت دهد)
        # result = response.json()
        # print(result)
        # return result
        pass
        # requests.get(result)
    else:
        print(f"Error: {response.status_code}")
        return 0
is_name = "@نام_و_نام_خانوادگی"
def send_group_sms(dfData,kind = task_name.update_birthday,msg="تست"):
    # ls= []
    # ls.append({"name":"hosein","mobile":"09139960164"})
   
    # dfData = pd.DataFrame(ls)
    if kind == task_name.update_birthday:
        this_indexs = get_index_boc(dfData)
        
        while len(dfData):
            
            this_mobile = dfData.iat[0,this_indexs.mobile]
            df_sms = dfData.loc[dfData[boc_class.mobile]==this_mobile]
            dfData = dfData.loc[dfData[boc_class.mobile]!=this_mobile]
            if len(df_sms):
                name = df_sms.iat[0,this_indexs.name]
                
                this_msg = msg.replace(is_name,name)
                
                
                send_sms(text_=this_msg,to_=this_mobile)
                time.sleep(0.04)
# send_sms()
# send_group_sms("test")