from django import forms
from .models import Device_Info, Farm_Info, Growth_Params

class Device_Form(forms.ModelForm):
    class Meta:
        model = Device_Info
        fields = "__all__"

class Farm_Info_Form(forms.ModelForm):
    class Meta: 
        model = Farm_Info
        fields = "__all__"

class Growth_Params_Form(forms.ModelForm):
    class Meta:
        model = Growth_Params
        fields = ['germination_time', 'seeding_ec', 'ec', 'progress_date', 'temparature', 'ph', 'humidity','light_hr','nutrientA', 'nutrientB', 'nutrientC', 'nutrientD', 'light_lux', 'do', 'co2']
