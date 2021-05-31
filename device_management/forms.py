from django import forms
from .models import Device_Info, Farm_Info

class Device_Form(forms.ModelForm):
    class Meta:
        model = Device_Info
        fields = ['device_serial', 'device_no', 'device_detail', 'device_name']