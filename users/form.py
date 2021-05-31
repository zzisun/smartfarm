from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from django.forms import fields, widgets
from .models import Users
from django.contrib.auth.hashers import check_password

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(label="Email address", required=True)
    mobile_number = forms.CharField(max_length=64, label="Mobile number")

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'mobile_number','email', 'password']

    def save(self, commit: True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class RegisterForm(forms.Form):
    first_name = forms.CharField(
        error_messages={'required': "Input First Name."},
        max_length=64, label="First name"
    )
    last_name = forms.CharField(
        error_messages={'required': "Input Last Name."},
        max_length=64, label="Last name"
    )
    mobile_number = forms.CharField(
        error_messages={'required': "Input Mobile Number."},
        max_length=64, label="Mobile number"
    )
    email = forms.EmailField(
        error_messages={'required': "Input Email."},
        max_length=64, label="Email address"
    )
    password = forms.CharField(
        error_messages={'required': "Input Password"},
        widget=forms.PasswordInput, label="Password"
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        mobile_number = cleaned_data.get('mobile_number')
        password = cleaned_data.get('password')



class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={'required': 'Input Email.'},
        max_length=64, label="email"
    )
    password = forms.CharField(
        error_messages={'required': "Input Password"},
        max_length=128, label="password", widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = Users.objects.get(email=email)
            except Users.DoesNotExist:
                self.add_error('email', "Couldn't find your account.")
                return

            if not check_password(password, user.password):
                self.add_error('password', 'Wrong password.')
