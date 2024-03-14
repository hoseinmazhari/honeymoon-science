from django.urls import path,include
from . import views
app_name = "product_app"
urlpatterns = [
    
    path('',views.product_page,name="product_page"),
    path('order_point/',views.order_point,name="order_point"),
    
]
