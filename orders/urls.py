from django.urls import path
from . import views


urlpatterns = [
    path('cart', views.show_cart,name='cart'),
    path('add_to_cart', views.add_to_cart,name='add_to_cart'),
    path('remove_cart_product/<pk>',views.remove_item_from_cart,name='remove_cart_product'),
    path('checkout',views.checkout,name='checkout'),
    path('orders',views.get_orders,name='orders')
]