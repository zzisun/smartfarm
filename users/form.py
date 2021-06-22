from users.models import Users
from django.contrib.auth import authenticate, get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from django.forms import fields, widgets
from django.contrib.auth.hashers import check_password

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(label="Email address", required=True)
    mobile_number = forms.CharField(max_length=64, label="Mobile number")

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'mobile_number','email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class LoginForm(forms.ModelForm):
    password  = forms.CharField(label= 'Password', widget=forms.PasswordInput)

    class Meta:
        model  =  Users
        fields =  ('email', 'password')
        widgets = {
                   'email':forms.TextInput(attrs={'class':'form-control'}),
                   'password':forms.TextInput(attrs={'class':'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['password']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean(self):
        if self.is_valid():

            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')

class EditProfileForm(UserChangeForm):
    class Meta: 
        model = Users
        fields = [
            'first_name', 
            'last_name',
            'email', 
            'mobile_number'
            ]