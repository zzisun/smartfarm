from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, first_name, last_name, mobile_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            mobile_number = mobile_number
        )

        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, mobile_number, password):
        user = self.create_user(
            email,
            password=password,
            first_name = first_name,
            last_name = last_name,
            mobile_number = mobile_number
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    

class Users(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    mobile_number = models.TextField(verbose_name='mobile number', max_length=12, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin