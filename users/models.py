from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.TextField(max_length=12, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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