from django.urls import path,include
from . import views
app_name = "honeymoonatr_app"
urlpatterns = [
    
    path('',views.honeymoonatr_panel,name="honeymoonatr_panel"),
    # path('update/',views.update_db,name="update_db"),
    # path('arad/',views.arad_detail,name="arad_detail"),
]
