# Generated by Django 3.2.3 on 2021-05-26 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210526_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='mobile_number',
            field=models.TextField(blank=True, max_length=12, verbose_name='mobile number'),
        ),
    ]
