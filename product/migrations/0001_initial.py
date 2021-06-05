# Generated by Django 3.2.3 on 2021-06-02 07:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort', models.CharField(default='', max_length=255, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Product name')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('description', models.TextField(default='', verbose_name='Description')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('stock', models.IntegerField(default=0, verbose_name='Stock')),
                ('registered_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Registered Date')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='product.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product',
                'db_table': 'shoppingmall_Product',
            },
        ),
    ]
