from django.contrib import admin
from .models import Order, Cart

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity','ordered_date')

class CartAdmin(admin.ModelAdmin):
    list_display = ('user','product','quantity')
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)