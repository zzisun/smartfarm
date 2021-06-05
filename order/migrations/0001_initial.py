# Generated by Django 3.2.3 on 2021-06-02 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='quantity')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='product_amount')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_date', models.DateTimeField(auto_now_add=True, verbose_name='order_date')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='product_amount')),
                ('status', models.CharField(choices=[('Proc', 'Processing'), ('Deli', 'Delivered')], default='Proc', max_length=4, verbose_name='status')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'order',
                'db_table': 'Shoppingmall_Order',
            },
        ),
    ]
