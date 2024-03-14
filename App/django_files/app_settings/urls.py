from django.urls import path,include
from . import views
app_name = "app_setting"
urlpatterns = [
    
    path('',views.list,name="list"),
    path('app_address/',views.app_address,name="app_address"),
    path('sites/',views.sites,"sites")
    # path('arad/',views.arad_detail,name="app_xpath"),
]
