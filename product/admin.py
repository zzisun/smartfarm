from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Category, Addfeature

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock','category')
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('sort',)
admin.site.register(Category, CategoryAdmin)

class AddfeatureAdmin(admin.ModelAdmin):
    list_display = ('product','option','price')
admin.site.register(Addfeature, AddfeatureAdmin)