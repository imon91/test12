# Generated by Django 2.2.7 on 2019-12-07 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomadminapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modify', to=settings.AUTH_USER_MODEL),
        ),
    ]
