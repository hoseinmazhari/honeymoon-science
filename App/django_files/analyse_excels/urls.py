from django.urls import path,include
from . import views
app_name = "analyse_excels_app"
urlpatterns = [
    
    path('',views.analyse_list,name="analyse_list"),
    path('factors_count/',views.factors_count,name="factors_count"),
    # path('recieve/',views.recieve,name="recieve"),
    path('merge_base_factors/',views.merge_base_factors,name="merge_factors_hamyar_with_hesabro"),
    path('merge_factors_customers/',views.merge_factors_customers,name="merge_final_merged_factors_with_customers"),
]
