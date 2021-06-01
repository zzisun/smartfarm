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

    def create_user(self, email, password, first_name = '', last_name = '', mobile_number = '', **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)

        user = self.model(email=email, first_name = first_name, last_name = last_name, mobile_number = mobile_number, **extra_fields)
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

class Users(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    mobile_number = models.CharField(verbose_name='mobile number', max_length=12, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

# class UserManager(BaseUserManager):
#     """
    # Custom user model manager where email is the unique identifiers
    # for authentication instead of usernames.
    # """

    # def create_user(self, email, password, first_name = '', last_name = '', mobile_number = '', **extra_fields):
    #     """
    #     Create and save a User with the given email and password.
    #     """
    #     if not email:
    #         raise ValueError(_('The Email must be set'))
    #     email = self.normalize_email(email)

    #     user = self.model(email=email, first_name = first_name, last_name = last_name, mobile_number = mobile_number, **extra_fields)
    #     user.set_password(password)
    #     user.save()
    #     return user

    # def create_superuser(self, email, password, **extra_fields):
    #     """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True.'))
#         return self.create_user(email, password, **extra_fields)

# class Users(AbstractUser):
#     username = None
#     email = models.EmailField(_('email address'), unique=True)
#     mobile_number = models.CharField(verbose_name='mobile number', max_length=12, blank=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     objects = UserManager()

#     def __str__(self):
#         return self.email


# class UserManager(BaseUserManager):
#     """
#     Custom user model manager where email is the unique identifiers
#     for authentication instead of usernames.
#     """
#     def _create_user(self, email, first_name="", last_name="", mobile_number="", password=None, **extra_fields):
#         if not email:
#             raise ValueError('Users must have an email address')
#         email = self.normalize_email(email)

#         user = self.model(
#             email=email,
#             first_name = first_name,
#             last_name = last_name,
#             mobile_number = mobile_number
#         )

#         user.password = make_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         # user = self.create_user(
#         #     email,
#         #     password=password,
#         #     first_name = first_name,
#         #     last_name = last_name,
#         #     mobile_number = mobile_number
#         # )
#         # user.is_admin = True
#         # user.save(using=self._db)
#         # return user
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#         return self._create_user(email, password, **extra_fields)


# class Users(AbstractUser):
#     username = None
#     email = models.EmailField(_('email address'), unique=True)
#     mobile_number = models.TextField(verbose_name='mobile number', max_length=12, blank=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = UserManager()

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin