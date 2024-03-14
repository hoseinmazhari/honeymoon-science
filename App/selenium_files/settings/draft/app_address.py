hesabro_domain = "https://hesabro.ir/@hm"
# from main import hesabro_domain
# 
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
