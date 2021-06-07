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
from requests_oauthlib import OAuth1
from urllib.parse import urlencode
from rest_framework.views import APIView
from django.http.response import HttpResponseRedirect, HttpResponse
from django.conf import settings
import requests
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, "users/sign_in1.html")
def menu(request):
    return render(request, "users/menu.html")

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
    return redirect('device_management:mypage')


@api_view(['GET'])
def userAPI(request):
    userlist = list(User.objects.all())
    serializer = UserSerializer(userlist, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userAPI(request):
    userlist = list(Users.objects.all())
    serializer = UserSerializer(userlist, many=True)
    return Response(serializer.data)

# OAuth by Twitters
class TwitterAuthRedirectEndpoint(APIView):
    def get(self, request, *args, **kwargs):
        try:
            oauth = OAuth1(
                      client_key=settings.TWITTER_API_KEY,
                      client_secret=settings.TWITTER_API_SECRET_KEY,
            )
            print(oauth)
             #Step one: obtaining request token
            request_token_url = "https://api.twitter.com/oauth/request_token"
            data = urlencode({
                "oauth_callback": settings.TWITTER_AUTH_CALLBACK_URL
            })
            response = requests.post(request_token_url, auth=oauth, data=data)
            response.raise_for_status()
            response_split = response.text.split("&")
            oauth_token = response_split[0].split("=")[1]
            oauth_token_secret = response_split[1].split("=")[1]

                #Step two: redirecting user to Twitter
            twitter_redirect_url = (f"https://api.twitter.com/oauth/authenticate?oauth_token={oauth_token}")
            return HttpResponseRedirect(twitter_redirect_url)
        except ConnectionError:
            html="<html><body>You have no internet connection</body></html>"
            return HttpResponse(html, status=403)
        except:
            html="<html><body>Something went wrong.Try again.</body></html>"
            return HttpResponse(html, status=403)

class TwitterCallbackEndpoint(APIView):
    def get(self, request, *args, **kwargs):
        try:
            oauth_token = request.query_params.get("oauth_token")
            oauth_verifier = request.query_params.get("oauth_verifier")
            oauth = OAuth1(
                settings.TWITTER_API_KEY,
                client_secret=settings.TWITTER_API_SECRET_KEY,
                resource_owner_key=oauth_token,
                verifier=oauth_verifier,
            )
            res = requests.post(
                f"https://api.twitter.com/oauth/access_token", auth=oauth
            )
            res_split = res.text.split("&")
            oauth_token = res_split[0].split("=")[1]
            oauth_secret = res_split[1].split("=")[1]
            user_id = res_split[2].split("=")[1] if len(res_split) > 2 else None
            user_name = res_split[3].split("=")[1] if len(res_split) > 3 else None
            # store oauth_token, oauth_secret, user_id, user_name
            redirect_url = "http://158.247.227.73:8000/twitter/share/"
            return HttpResponseRedirect(redirect_url)
        except ConnectionError:
            return HttpResponse(
                "<html><body>You have no internet connection</body></html>", status=403
            )

        except:
            return HttpResponse(
                "<html><body>Something went wrong.Try again. redirect problem</body></html>", status=403
            )
