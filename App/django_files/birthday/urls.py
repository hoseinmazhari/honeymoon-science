from django.urls import path,include
from . import views
app_name = "birthday_app"
urlpatterns = [
    
    path('',views.birthday_page,name="birthday_page"),
    path('update/',views.update_db,name="update_db"),
    path('arad/',views.arad_detail,name="arad_detail"),
]
