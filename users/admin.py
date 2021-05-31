from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib import admin
from .models import Users

class UsersAdmin(admin.ModelAdmin):
    list_display = ('email','first_name')

admin.site.register(Users, UsersAdmin)
admin.site.unregister(Group)