# Generated by Django 3.2 on 2021-05-27 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0004_rename_deivce_password_device_info_device_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='mock_params',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=15)),
                ('ph', models.FloatField()),
                ('temp', models.IntegerField()),
            ],
        ),
    ]
