from django import forms
from .models import Device_Info, Farm_Info

class Device_Form(forms.ModelForm):
    class Meta:
        model = Device_Info
        fields = "__all__"

class Farm_Info_Form(forms.ModelForm):
    class Meta: 
        model = Farm_Info
        fields = "__all__"
