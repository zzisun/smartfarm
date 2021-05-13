from django import forms
from .models import Users
from django.contrib.auth.hashers import check_password


class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={'required': "Input Email."},
        max_length=64, label="email"
    )
    name = forms.CharField(
        error_messages={'required': "Input Name."},
        max_length=64, label="name"
    )
    password = forms.CharField(
        error_messages={'required': "Input Password"},
        widget=forms.PasswordInput, label="Password"
    )
    re_password = forms.CharField(
        error_messages={'required': "Input Password one more"},
        widget=forms.PasswordInput, label="Input re_password"
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        name = cleaned_data.get('name')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', 'Those passwords didn’t match.')


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