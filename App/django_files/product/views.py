from django.shortcuts import render
import os,sys
sys.path.append("..")
from selenium_files.settings.run_app import task_selector
from selenium_files.settings import app_tasks as atk
# Create your views here.
def price_with_t(request):
    pass
def order_point(request):
    result = {"result":"stoped"}
    if request.method == 'POST':
        data = request.POST
        action = data.get("act")
        if action == "run":
            # driver = webdriver.Firefox()
            task_selector(atk.task_name.set_order_point)
        # driver.get('http://aradpayamak.net')
            # driver.get("https://honeymoonatr.com")
                # for t in driver.title:
            # result = {"result":(f"عنوان سایت بارگزاری شده: {driver.title}") }
        else:
            print("stop")
            # driver.close()
        
        # return redirect(("arad/"))
    # message ={"messages":"test"}
    
    return render(request,'product/update_order_point.html',result)
def product_page(request):
    return render(request,'product/product_page.html')