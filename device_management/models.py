from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case

# Create your models here.
class Device_Info(models.Model):
    device_serial = models.IntegerField()
    device_model = models.CharField(default="", null=False, max_length=15)
    device_name = models.CharField(default="", max_length=15)
    device_detail = models.CharField(max_length=100, default="")
    device_ip_address = models.CharField(max_length = 40, default="0.0.0.0")
    device_password = models.CharField(max_length = 20, default="0000")

class Farm_Info(models.Model):
    device_info = models.ForeignKey(Device_Info, on_delete=CASCADE)
    farm_type = models.CharField(max_length=15)
    farm_name = models.CharField(default="", max_length = 20)
    farm_capacity = models.IntegerField(default=1, null=False)
    farm_no = models.IntegerField(primary_key=True)

class Plant_Info(models.Model):
    farm_info = models.ForeignKey(Farm_Info, on_delete=CASCADE)
    crop_group = models.IntegerField() #0:lettuce 1:leafy green, 2:herbs, 3:fruits
    crop_name = models.CharField(max_length = 20, null=True)
    life_stage = models.IntegerField() #0:seed planting 1:germination 2:seeding 3:growth 4:harvest
    planting_date = models.DateField() #first date to plant seed

class Growth_Params(models.Model):
    device_info = models.ForeignKey(Device_Info, on_delete=CASCADE)
    germination_time = models.IntegerField()
    seeding_ec = models.FloatField()
    ec = models.FloatField()
    progress_date = models.IntegerField() #it means duration, in html, show not only duration, but also d-day
    temparature = models.IntegerField()
    ph = models.FloatField()
    humidity = models.FloatField()
    date = models.DateField() #very important, to draw time-cordinate graph
    plant_info = models.ForeignKey(Plant_Info, on_delete=CASCADE)
    light_hr = models.IntegerField() # light hour

    def __str__(self):
        return f"{self.ph} {self.humidity} {self.ec}"

class mock_params(models.Model):
    serial = models.CharField(max_length = 15)
    ph = models.FloatField()
    temp = models.IntegerField()

    def __str__(self):
        return f"{self.serial} {self.ph} {self.temp}"