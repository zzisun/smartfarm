# Generated by Django 3.2.3 on 2021-06-05 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0006_alter_farm_info_farm_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm_info',
            name='farm_name',
            field=models.CharField(default='farm2021-06-05-04:19:03-PM', max_length=30),
        ),
    ]
