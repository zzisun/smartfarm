# Generated by Django 3.2 on 2021-05-26 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0003_auto_20210526_1924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device_info',
            old_name='deivce_password',
            new_name='device_password',
        ),
    ]
