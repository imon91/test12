from django.contrib import admin

# Register your models here.
from ecom.models import Order, CustomerRegistration

admin.site.register(Order)
admin.site.register(CustomerRegistration)