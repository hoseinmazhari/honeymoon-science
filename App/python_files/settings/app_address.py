hesabro_domain = "https://hesabro.ir/@hm"
# from main import hesabro_domain
# 
arad_payamek_domain = "http://aradpayamak.net"
class urls_arad():
    class phone_book():
        contact_groups = "http://aradpayamak.net/APPs/SMS/?cmp=PhoneBook&st=PhoneBookCategory"
        send_sms = 'http://aradpayamak.net/APPs/SMS/?cmp=SendDynamic&st=SendDynamic&action=sendSMSI'
    class simple_send_sms():
        send_page = 'http://aradpayamak.net/APPs/SMS/?cmp=Send&st=SendSMS'
class url_address():
    class user_detail():
        coin = f"{hesabro_domain}/customer/coin?id="
    class product():
        create_product = f"{hesabro_domain}/product-main/add-variety?copy_id=0&referrer=https%3A%2F%2Fhesabro.ir%2F%40hm%2Fproduct"
    class create_report():
        birthday = f"{hesabro_domain}/report-customer/index"
    class random_page():
        pages = {
            "random":{
                "1" : "/tags",
                "2" : "/settings/index?category=1",
                "3" : "/version/index",
                "4" : "/sms-report/index",
                "5" : "/ipg",
                "6" : "/comments-type",
                "7" : "/education-course",
                "8" : "/factor-report/sale",
                "9" : "/product/sale-report",
                "10" : "/product/buy-sale-review-report?factor_type=4"}
            }
urls={
    "user_detail":{
        "coin": f"{hesabro_domain}/customer/coin?id="
    },
    "product":{
    "create_product" : f"{hesabro_domain}/product-main/add-variety?copy_id=0&referrer=https%3A%2F%2Fhesabro.ir%2F%40hm%2Fproduct"
    },
    "birthday":{
        "create_rpt": f"{hesabro_domain}/report-customer/index"
    }
    ,
    "random":{
        "1" : "/tags",
        "2" : "/settings/index?category=1",
        "3" : "/version/index",
        "4" : "/sms-report/index",
        "5" : "/ipg",
        "6" : "/comments-type",
        "7" : "/education-course",
        "8" : "/factor-report/sale",
        "9" : "/product/sale-report",
        "10" : "/product/buy-sale-review-report?factor_type=4"
    }
}
def get_address(part,element,id):
    return f"{urls[part][element]}{id}"
def get_rnd_page(element):
    element = str(element)
    return f"{hesabro_domain}{urls['random'][element]}"
