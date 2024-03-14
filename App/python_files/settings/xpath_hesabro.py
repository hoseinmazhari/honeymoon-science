
 
class login_form():
    number = "//input[@id='loginform-number']"
    authenticator = "//input[@id='loginform-authenticator']",
    password = "//input[@id='loginform-password']",
class searchbar():
    mobile = "//span[@id='select2-shortcutCustomerName-container']",
    merchandise = "//span[@id='select2-shortcutChecks-container']//span[1]",
class create_reportcustomer():
    btn_createRpt = '/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div/a'
    title = '//*[@id="reportcustomer-title"]'
    customer_type = '//*[@id="reportcustomer-customer_type"]'
    birthdayfromday = '//*[@id="reportcustomer-birthdayfromday"]'
    birthdaytoday = '//*[@id="reportcustomer-birthdaytoday"]'
    birthdaymonth = '//*[@id="reportcustomer-birthdaymonth"]'
    birthdaytomonth = '//*[@id="reportcustomer-birthdaytomonth"]'
    birthdayfromyear = '//*[@id="reportcustomer-birthdayfromyear"]'
    birthdaytoyear = '//*[@id="reportcustomer-birthdaytoyear"]'
    customer_sex = '//*[@id="reportcustomer-customer_sex"]'
    customer_nationality = '//*[@id="reportcustomer-customer_nationality"]'
    customer_name = '//*[@id="reportcustomer-customer_name"]'
    identified = '//*[@id="reportcustomer-identified"]'
    work = '/html/body/div[2]/div/div[2]/div[2]/form/div[1]/div/div[13]/div/span/span[1]/span/ul/li/input'
    des = '//*[@id="reportcustomer-des"]'
    save = '/html/body/div[2]/div/div[2]/div[2]/form/div[2]/button'
    download = '/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/a'
    class dataReport():
        tbody = '/html/body/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div/table/tbody'
        next_p = '/html/body/div[2]/div/div[2]/div[2]/div/div[2]/div/div/ul/li[8]/a'
                #  /html/body/div[2]/div/div[2]/div[2]/div/div[2]/div/div/ul/li[8]/span
 
xpath = {
    
   

    
    'user_detail':{
        'coin':"//a[text()='سکه های مشتری']",
        'coin_table': "//table",
        'coin_table_tr':"//tr",
        # 'coin_title' : f"//td[text()='{Initial_charge}']"
    },
    "merchandise":{
        "list" :  "//i[@class='ti-package']",
        
        "search_btn": "//a[contains(.,' جستجو')]",
        "productsearch_sh_name": "//input[@id='productsearch-sh_name']",
        "productsearch-abandoned":"//input[@id='productsearch-abandoned']",
        "table":"//table",
        # productsearch-abandoned
        "btn" :"//table//button",
        "menu_items": "//div[@class='dropdown-menu show']//a",
        # "update_btn" : "//a[@class='dropdown-item'][contains(text(),'بروز رسانی')]",
        # "//button"
        # "//div[@id='w13']//a[@class='dropdown-item'][contains(text(),'بروز رسانی')]"
        "act_button": "//button[@id='w0-button']",
        "update_btn": "//a[contains(text(),'بروز رسانی')]",
        "salePrice": "//input[@id='product-price1']",
        "buyPrice": "//input[@id='product-price4']",
        "check_exit" : "//input[@id='product-abandoned']",
        "btn_submit": "//button[@type='submit']",
        "more_details": '//*[@id="accordion"]/div[1]/h4/a',
        "order_point": '//*[@id="product-order_point_inventory"]' ,#'/html/body/div[2]/div/div[2]/form/div/div[1]/div[2]/div[2]/div/div[3]/div/input'
        "merchandise_unit": "/html/body/div[2]/div/div[2]/form/div/div[1]/div[1]/div[11]/div/select",
        "short_name_input" : "//*[@id='product-sh_name']",
        "btn_add_other_unit" : "/html/body/div[2]/div/div[2]/form/div/div[1]/div[4]/div[1]/div/div/div[1]/button",
        "input_title_other_unit": "/html/body/div[2]/div/div[2]/form/div/div[1]/div[4]/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div/input",
        "cr_form_category" : "//*[@id='select2-productmain-category-container']",
        "cr_form_category_li_exclusive": "/html/body/span/span/span[2]/ul/li[3]",
        "cr_form_category_li_non_exclusive": "/html/body/span/span/span[2]/ul/li[6]",
        "cr_form_brand" : '/html/body/div[2]/div/div[2]/form/div/div[1]/div[1]/div[1]/div/div[2]/div/span/span[1]/span',
        # "cr_form_honeymoon_brand": '//*[@id="select2-productmain-brand-container"]',
        "cr_form_title": "/html/body/div[2]/div/div[2]/form/div/div[1]/div[1]/div[1]/div/div[3]/div/input",
        # "cr_form_short_name": "/html/body/div[2]/div/div[2]/form/div/div[1]/div[1]/div[2]/div/input[@id='product-abandoned']",
        "cr_form_store_price": "/html/body/div[2]/div/div[2]/form/div/div[1]/div[1]/div[4]/div/input[@id='product-price1']",
        "cr_form_buy_price": "/html/body/div[2]/div/div[2]/form/div/div[1]/div[1]/div[5]/div/input[@id='product-price4']",
        "cr_form_unit": '//*[@id="product-unit_id"]',
        "cr_form_btn_add_unit" : '/html/body/div[2]/div/div[2]/form/div/div[1]/div[4]/div[1]/div/div/div[1]/button',
        "cr_form_txt_unit_title" : '//*[@id="subunitsform-0-title"]',
        "cr_form_chk_is_ok": '/html/body/div[2]/div/div[2]/form/div/div[1]/div[4]/div[1]/div/div/div[2]/div/div[2]/div/div[5]/div[1]/div/input[2]'


    },#
    "store_handling":{
        "kind": '//*[@id="storehandlingsearch-store_handling_status"]', # /html/body/div[2]/div/div[2]/div[2]/div/div[1]/form/div/div/div[1]/div/select
        "no_handling_status": '//*[@id="storehandlingsearch-store_handling_status"]/option[5]', # /html/body/div[2]/div/div[2]/div[2]/div/div[1]/form/div/div/div[1]/div/select/option[5]
        "search_btn": '//*[@id="store-handling-view-search"]/div/div/div[2]/button' , # /html/body/div[2]/div/div[2]/div[2]/div/div[1]/form/div/div/div[2]/button
        

    }

}



def get_xpath(part,element):
    return xpath[part][element]

# print()