# Generated by Django 3.2.3 on 2021-06-03 14:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device_Info',
            fields=[
                ('device_serial', models.IntegerField(primary_key=True, serialize=False)),
                ('device_model', models.CharField(default='', max_length=15)),
                ('device_name', models.CharField(default='', max_length=15)),
                ('device_detail', models.CharField(default='', max_length=100)),
                ('device_ip_address', models.CharField(default='0.0.0.0', max_length=40)),
                ('device_password', models.CharField(default='0000', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Farm_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('farm_type', models.CharField(max_length=15)),
                ('farm_name', models.CharField(default='farm2021-06-03-11:40:39-PM', max_length=30)),
                ('farm_capacity', models.IntegerField(default=1)),
                ('farm_plant_num', models.IntegerField(default=0)),
                ('farm_model_no', models.CharField(default='Smart farm 20', max_length=15)),
                ('device_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device_management.device_info')),
            ],
        ),
        migrations.CreateModel(
            name='mock_params',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=15)),
                ('ph', models.FloatField()),
                ('temp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Plant_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_group', models.CharField(max_length=15)),
                ('crop_name', models.CharField(max_length=20, null=True)),
                ('life_stage', models.CharField(max_length=15)),
                ('planting_date', models.DateField(default=datetime.date(2021, 6, 3))),
                ('farm_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device_management.farm_info')),
            ],
        ),
        migrations.CreateModel(
            name='Growth_Params',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('germination_time', models.IntegerField()),
                ('seeding_ec', models.FloatField()),
                ('ec', models.FloatField()),
                ('progress_date', models.IntegerField()),
                ('temparature', models.IntegerField()),
                ('ph', models.FloatField()),
                ('humidity', models.FloatField()),
                ('date', models.DateField()),
                ('light_hr', models.IntegerField()),
                ('device_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device_management.device_info')),
                ('plant_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device_management.plant_info')),
            ],
        ),
    ]
