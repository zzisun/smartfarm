from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(models.Model):
    email = models.CharField(verbose_name="email", max_length = 128, unique=True)
    first_name = models.CharField(verbose_name="first name", max_length=30, blank=True)
    last_name = models.CharField(verbose_name="last name", max_length=30, blank=True)
    password = models.CharField(max_length = 100, verbose_name = "password" )
    mobile_number = models.CharField(max_length=12, verbose_name="mobile number", blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', default=datetime.now)
    level = models.CharField(verbose_name="level", max_length=8,
    choices = (('admin', 'admin'), ('user', 'user')))

    def __str__(self):
        return self.email

    class Meta:
        db_table = "Shoppingmall_users"
        verbose_name = "user"
        verbose_name_plural = "user"

# class CustomUserManager(BaseUserManager):
#     def create_user(elf, email, first_name, last_name, phone_number, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email = self.normalize_email(email),            
#             first_name = first_name,
#             last_name = last_name,
#             phone_number = phone_number
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, first_name, last_name, phone_number, password=None):
#         user = self.create_user(
#             email = self.normalize_email(email),            
#             first_name = first_name,
#             last_name = last_name,
#             phone_number = phone_number
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user


# class CustomUser(AbstractUser):
#     mobile_number = models.TextField(verbose_name='mobile number', max_length=12, blank=True)
#     # class Meta:
#     #     db_table = "user"