from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

# class Users(models.Model):
#     username = None
#     email = models.EmailField(verbose_name="email", max_length = 128, unique=True)
#     first_name = models.CharField(verbose_name="first name", max_length=30, blank=True)
#     last_name = models.CharField(verbose_name="last name", max_length=30, blank=True)
#     password = models.CharField(max_length = 100, verbose_name = "password" )
#     mobile_number = models.CharField(max_length=12, verbose_name="mobile number", blank=True)
#     date_joined = models.DateTimeField(verbose_name='date joined', default=datetime.now)
#     level = models.CharField(verbose_name="level", max_length=8,
#     choices = (('admin', 'admin'), ('user', 'user')))

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email

#     class Meta:
#         db_table = "Shoppingmall_users"
#         verbose_name = "user"
#         verbose_name_plural = "user"

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    mobile_number = models.TextField(verbose_name='mobile number', max_length=12, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email