from django.urls import path
from . import views


urlpatterns = [
    path('account', views.show_account,name='account'),
    path('sign_out', views.sign_out,name='sign_out'),
]