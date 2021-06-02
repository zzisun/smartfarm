from django.contrib import admin
from .models import Device_Info, Farm_Info, Plant_Info, Growth_Params
# Register your models here.

admin.site.register(Device_Info)
admin.site.register(Farm_Info)
admin.site.register(Plant_Info)
admin.site.register(Growth_Params)
