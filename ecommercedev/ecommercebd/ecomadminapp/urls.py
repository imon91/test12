from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from ecomadminapp import views
from django.conf.urls.static import static

app_name = 'ecomadminapp'
urlpatterns = [
    path('', views.index, name="index"),
    path('logout/', views.logout, name="logout"),
    path('login/', views.login, name="login"),
    path('company_detail/', views.company_detail, name="company_detail"),
    path('product_category/', views.product_category, name="product-category"),

]

