from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Category(models.Model):
    sort = models.CharField(max_length=255, verbose_name="Category", default='')

    def __str__(self):
        return '{}'.format(self.sort)

class Product(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="Product name", default='')
    #text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Category', default='')
    price = models.IntegerField(verbose_name="Price", default=0)
    description = models.TextField(verbose_name="Description", default='')
    image = models.ImageField(upload_to='images/', null = True)
    stock = models.IntegerField(verbose_name="Stock" ,default=0)
    registered_date = models.DateTimeField(verbose_name="Registered Date",default=timezone.now)
    #created_date = models.DateTimeField(
    ##       default=timezone.now)
    #published_date = models.DateTimeField(
    #        blank=True, null=True)

    def publish(self):
        self.registered_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "shoppingmall_Product"
        verbose_name = "Product"
        verbose_name_plural = "Product"