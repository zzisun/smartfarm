from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    email = models.CharField(verbose_name="email", max_length = 128)
    name = models.CharField(verbose_name="user name", max_length=30)
    password = models.CharField(max_length = 100, verbose_name = "password" )
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="registerd date")
    level = models.CharField(verbose_name="level", max_length=8,
    choices = (('admin', 'admin'), ('user', 'user')))

    def __str__(self):
        return self.email

    class Meta:
        db_table = "Shoppingmall_users"
        verbose_name = "user"
        verbose_name_plural = "user"
