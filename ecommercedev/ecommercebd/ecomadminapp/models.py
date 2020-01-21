from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
# Create your models here.
from registration.models import CompanyRegistration


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=250)
    image = models.FileField(upload_to='documents/product', blank=True, null=True)
    is_active = models.NullBooleanField(default=True)
    is_delete = models.NullBooleanField(default=False)
    created = models.DateTimeField(null=True)
    modified = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='create', null=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modify', null=True)

    def __str__(self):
        return self.name


class Promotion(models.Model):
    name = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=250)
    is_active = models.NullBooleanField(default=True)
    is_delete = models.NullBooleanField(default=False)
    created = models.DateTimeField(null=True)
    modified = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    company = models.ForeignKey(CompanyRegistration, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    discount_price = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=250)
    stock = models.IntegerField(max_length=100)
    photo = models.FileField(upload_to='documents/employee', blank=True, null=True)
    price = models.FloatField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    created = models.DateTimeField(null=True)
    is_active = models.NullBooleanField(default=False)
    is_delete = models.NullBooleanField(default=False)
    modified = models.DateTimeField(null=False)

    def __str__(self):
        return self.name

#
# class Transection(models.Model):
#
#     product =  models.ForeignKey(Product, null=True)
#     quantity = models.IntegerField(max_length=100)
#     created = models.DateTimeField(null=True)
#     is_active = models.NullBooleanField(default=False)
#     is_delete = models.NullBooleanField(default=False)
#     modified = models.DateTimeField(null=False)

class PhotoSlider(models.Model):
    title = models.CharField(max_length=50)
    photo = models.FileField()
    link = models.CharField(max_length=500)
    order = models.IntegerField()
    created = models.DateTimeField(null=True)
    is_active = models.NullBooleanField(default=False)
    is_delete = models.NullBooleanField(default=False)
    modified = models.DateTimeField(null=False)
