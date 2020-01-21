from django.contrib import admin
from django.urls import path, include

from registration import views
app_name = 'registration'
urlpatterns = [
    path('', views.index, name="registration"),  #For registration
    path('login/', views.login, name="login"),
    path('password/', views.password_update, name="password"),

]
