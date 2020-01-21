from django.conf import settings
from django.db import models


# Create your models here.
class CompanyRegistration(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bank_account = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=300)
    descriptions = models.CharField(max_length=300)
    image = models.FileField(upload_to='documents/company', blank=True, null=True)
    contact_number = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    created = models.DateTimeField(null=True)
    is_active = models.NullBooleanField(default=True)
    is_delete = models.NullBooleanField(default=False)
    modified = models.DateTimeField(null=True)
    def __str__(self):
        return self.name