from django.contrib import admin
from .models import *
import datetime

# Register your models here.

admin.site.register(Promotion)
admin.site.register(Product)


class PhotoSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_filter = ("title",)


admin.site.register(PhotoSlider, PhotoSliderAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'descriptions', 'created', 'created_by', 'modified', 'modified_by')
    list_filter = ("name",)
    exclude = ('created', 'created_by', 'modified', 'modified_by')

    def save_model(self, request, obj, form, change):
        if change:
            obj.modified = datetime.datetime.now()
            obj.modified_by = request.user
        else:
            obj.created = datetime.datetime.now()
            obj.created_by = request.user
        obj.save()


admin.site.register(ProductCategory, ProductCategoryAdmin)
