from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('product_list',views.product_list,name='product_list'),
    path('product_detail/<int:pro_id>/',views.product_detail,name='product_detail'),
    path('migrate',views.run_migrate,name='migrate'),
]