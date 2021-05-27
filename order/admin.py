from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity','ordered_date')

admin.site.register(Order, OrderAdmin)