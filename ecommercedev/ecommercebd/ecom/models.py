from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from ecomadminapp.models import Product


class Order(models.Model):
    STATUS_CATEGORY = (
        ('1', 'cart'),
        ('2', 'place_order'),
        ('3', 'approve'),
        ('4', 'delivery'),
        ('5', 'receive')

    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=100, choices=STATUS_CATEGORY)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(null=True)
    modified = models.DateTimeField(null=False)


class CustomerRegistration(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bank_account = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    address = models.CharField(max_length=300)
    descriptions = models.CharField(max_length=300)
    image = models.FileField(upload_to='documents/user', blank=True, null=True)
    contact_number = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)

    def __str__(self):
        return self.name
