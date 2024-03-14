from django.urls import path,include
from . import views
app_name = "get_the_report_app"
urlpatterns = [
    
    path('',views.get_report_from_hesabro,name="get_report"),
    
    
]