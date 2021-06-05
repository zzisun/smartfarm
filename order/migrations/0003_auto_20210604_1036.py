# Generated by Django 3.2.3 on 2021-06-04 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='option',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Option'),
        ),
        migrations.AddField(
            model_name='order',
            name='option',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Option'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Proc', 'Processing'), ('Ship', 'Shipped'), ('On', 'On the way'), ('Deli', 'Delivered')], default='Proc', max_length=4, verbose_name='status'),
        ),
    ]
