from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.expressions import Case
from django.db.models.fields import DateField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import date
import time
from django.utils.translation import ugettext_lazy as _
#from .models import Plant_Info

# Create your models here.
class Device_Info(models.Model):
    device_user = models.ForeignKey('users.Users', verbose_name="user", on_delete=models.CASCADE, default='')
    device_serial = models.IntegerField(primary_key=True)
    device_model = models.CharField(default="", null=False, max_length=15)
    device_name = models.CharField(default="", max_length=15)
    device_detail = models.CharField(max_length=100, default="")
    device_ip_address = models.CharField(max_length = 40, default="0.0.0.0")
    device_password = models.CharField(max_length = 20, default="0000")


class Farm_Info(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', unique=True)
    device_info = models.ForeignKey(Device_Info, on_delete=CASCADE, related_name='farms')
    farm_type = models.CharField(max_length=15)

    farm_name = models.CharField(primary_key = False, max_length = 30, null=False, default="farm"+time.strftime('%Y-%m-%d-%I:%M:%S-%p'))

    farm_capacity = models.IntegerField(default=1, null=False)
    farm_plant_num = models.IntegerField(default = 0)
    farm_model_no = models.CharField(max_length = 15, default = "Smart farm 20")

     
class Plant_Info(models.Model):
    farm_info = models.ForeignKey(Farm_Info, on_delete=CASCADE, related_name='plants')
    crop_group = models.CharField(max_length = 15) 
    crop_name = models.CharField(max_length = 20, null=True)
    life_stage = models.CharField(max_length = 15) 

    planting_date = models.DateField(default = date.today()) #first date to plant seed
'''
@receiver(pre_save, sender = Plant_Info)
def plant_info_pre_save(sender, instance, **kwargs):
    plant_info = instance
    try:
        plant_info.farm_info
    except Farm_Info.DoesNotExist:
        print("Farm_Info does not Exist error, when create Plant_Info")
'''



class mock_params(models.Model):
    serial = models.CharField(max_length = 15)
    ph = models.FloatField()
    temp = models.IntegerField()
    ec = models.FloatField()
    nutrientA = models.FloatField()
    light_lux = models.IntegerField()
    date = models.DateField(default = date.today())

    def __str__(self):
        return f"{self.date} {self.serial} {self.ph} {self.temp} {self.ec} {self.light_lux}"


class Device_Interface(models.Model):
    device_info = models.ForeignKey(Device_Info, on_delete=CASCADE)
    ################ #-1:off, 1:on ###############################
    
    heater = models.IntegerField()
    light = models.IntegerField()
    nut_pump_auto = models.IntegerField()
    pumpA = models.IntegerField()
    pumpB = models.IntegerField()
    pumpC = models.IntegerField()
    pumpD = models.IntegerField()
    
    water_pump_auto = models.IntegerField()
    pump_water = models.IntegerField()
    
    oxy_pump_auto = models.IntegerField()
    air_pump = models.IntegerField()

    auto_air_contiditon_pump = models.IntegerField()
    cooler = models.IntegerField()
    fan = models.IntegerField()
    humidifier = models.IntegerField()
    co2_gen = models.IntegerField()
    
    
    ################ #0:off, 1:on ###############################


class mock_interface(models.Model):
    device_info = models.ForeignKey(Device_Info, on_delete=CASCADE)
    cooler = models.IntegerField()
    humidifier = models.IntegerField()
    co2_gen = models.IntegerField()
    air_pump = models.IntegerField()

class Growth_Params(models.Model):
    device_info = models.ForeignKey(Device_Info, on_delete=CASCADE, related_name='params')
    germination_time = models.IntegerField()
    seeding_ec = models.FloatField()
    ec = models.FloatField()
    progress_date = models.IntegerField() #it means duration, in html, show not only duration, but also d-day
    temparature = models.IntegerField()
    ph = models.FloatField()
    humidity = models.FloatField()
    date = models.DateField() #very important, to draw time-cordinate graph
    plant_info = models.ForeignKey(Plant_Info, on_delete=CASCADE)
    nutrientA = models.FloatField()
    nutrientB = models.FloatField()
    nutrientC = models.FloatField()
    nutrientD = models.FloatField()
    light_hr = models.IntegerField() # light hour
    light_lux = models.IntegerField()
    #do = models.FloatField()
    do = models.IntegerField() #D.O. type changed to integer!!
    co2 = models.IntegerField()


    def __str__(self):
        return f"{self.ph} {self.humidity} {self.ec}"


## add default status data for each crops later......
class Default_Status(models.Model):
    crop_name = models.CharField(max_length=20)
    germination_time_max = models.IntegerField()
    germination_time_min = models.IntegerField()
    seedling_ec = models.FloatField()
    temp_max = models.IntegerField()
    temp_min = models.IntegerField()
    ph_max = models.FloatField()
    ph_min = models.FloatField()
    humidity_max = models.FloatField()
    humidity_min = models.FloatField()
    light_hr_max = models.IntegerField()
    light_hr_min = models.IntegerField()
    ec_max = models.FloatField()
    ec_min = models.FloatField()
    harvesting_time = models.IntegerField() #means 'N days'
    do_max = models.IntegerField()
    do_min = models.IntegerField()
    co2_max = models.IntegerField()
    co2_min = models.IntegerField()
