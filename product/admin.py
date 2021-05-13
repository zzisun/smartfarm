from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock','image')
admin.site.register(Product, ProductAdmin)