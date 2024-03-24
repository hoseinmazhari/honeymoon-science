from django.shortcuts import render
from selenium_files.settings.run_app import task_selector
from selenium_files.settings import app_tasks as atk

# Create your views here.
def honeymoonatr_panel(request):
    result = {"result":"stoped"}
    if request.method == 'POST':
        data = request.POST
        action = data.get("act")
        # print(action)
        if action == "run":
            # driver = webdriver.Firefox()
                # print("run is ok")
                task_selector(atk.task_name.run_honeymoonatr)
        # driver.get('http://aradpayamak.net')
            # driver.get("https://honeymoonatr.com")
                # for t in driver.title:
            # result = {"result":(f"عنوان سایت بارگزاری شده: {driver.title}") }
        else:
            print("stop")
            # driver.close()
        
        # return redirect(("arad/"))
    # message ={"messages":"test"}
    
    
    return render(request,"honeymoonatr/panel.html",result)