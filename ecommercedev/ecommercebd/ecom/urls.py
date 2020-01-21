from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ecom import views
app_name = 'ecom'
urlpatterns = [
    path('', views.index, name="index"),
    path('product_detail/<int:id>', views.product_detail, name="product_detail"),
    path('ajax/add-cart/', views.addcart, name="add-cart"),
]