from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('' , views.home , name='home') , 
    #path('detail/<slug:product_slug>', views.productdetail, name='product_detail'),
]