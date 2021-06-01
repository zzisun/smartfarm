from django.contrib import auth
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from users import models
from .form import *

from .form import CreateUserForm
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail.message import EmailMessage

# for OAuth in twitter
# from requests_oauthlib import OAuth1
from urllib.parse import urlencode
from rest_framework.views import APIView
from django.http.response import HttpResponseRedirect, HttpResponse
from django.conf import settings

import requests
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, "users/sign_in1.html")

def resetPassword(request):
    return render(request, "users/sign_in3.html")
def checkEmail(request):
    return render(request, "users/sign_in4.html")
def createPassword(request):
    return render(request, "users/sign_in5.html")

def verifyAccount(request):
    return render(request, "users/sign_up2.html")
def success(request):
    return render(request, "users/sign_up3.html")
@csrf_exempt
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('mypage')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()

				return redirect('verify')
		context = {'form':form}
		return render(request, 'users/sign_up1.html', context)
@csrf_exempt
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('mypage')
    else:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('mypage')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {'form':form}
        return render(request, 'users/sign_in2.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def mypage(request):
    current_user = request.user
    messages.info(request, 'user: '+current_user.email)
    return render(request, 'users/status.html')


@api_view(['GET'])
def userAPI(request):
    userlist = list(User.objects.all())
    serializer = UserSerializer(userlist, many=True)
    return Response(serializer.data)

def send_email():
    subject = "메시지" 
    to = ['aaa@bbb.com'] 
    from_email = 'myaccount@gmail.com' 
    message = "메시지를 성공적으로 전송" 
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()