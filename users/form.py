from users.models import Users
from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from django.forms import fields, widgets
from django.contrib.auth.hashers import check_password

# class CreateUserForm(UserCreationForm):
# 	class Meta:
# 		model = User
# 		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(label="Email address", required=True)
    mobile_number = forms.CharField(max_length=64, label="Mobile number")

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'mobile_number','email', 'password1', 'password2']

    def save(self, commit: True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
