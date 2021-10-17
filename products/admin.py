from django.contrib import admin
from django.db import models
from .models import Product
class ProductAdminModel(admin.ModelAdmin):
    list_display = ['title','description','price']
admin.site.register(Product,ProductAdminModel)