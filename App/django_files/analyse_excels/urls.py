from django.urls import path,include
from . import views
app_name = "analyse_excels_app"
urlpatterns = [
    
    path('',views.analyse_list,name="analyse_list"),
    path('factors_count/',views.factors_count,name="factors_count"),
    path('recieve/',views.recieve,name="recieve"),
]
