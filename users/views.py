from django.contrib import auth
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from users import models

from users.models import Users
from .form import CreateUserForm, RegisterForm, LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.core.mail.message import EmailMessage



# for OAuth in twitter
from requests_oauthlib import OAuth1
from urllib.parse import urlencode
from rest_framework.views import APIView
from django.http.response import HttpResponseRedirect, HttpResponse
from django.conf import settings
import requests
from .tweepy import tweet_scrap

def home(request):
    return render(request, "users/sign_in1.html")
def signIn(request):
    return render(request, "users/sign_in2.html")
def signUp(request):
    return render(request, "users/sign_up1.html")
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
def mypage(request):
    return render(request, "users/status.html")

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
    # template_name = 'users/sign_up1.html'

        if request.method == 'POST':
          form = RegisterForm(request.POST)
          if form.is_valid:
              form.save()
              print(100)
              return redirect('verify')
        else:
            form = CreateUserForm()
            
        context = {'form':form}
        return render(request, 'users/sign_up1.html', context)


class RegisterView(FormView):
    template_name = 'users/sign_up1.html'
    form_class = CreateUserForm
    success_url = '/verify'

    def form_valid(self, form):
        user = Users(
            email=form.cleaned_data.get('email'),
            first_name=form.cleaned_data.get('first_name'),
            last_name=form.cleaned_data.get('last_name'),
            mobile_number=form.cleaned_data.get('mobile_number'),
            password=make_password(form.cleaned_data.get('password')),
            level='user'
        )
        print(user)
        user.save()

        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'users/sign_in2.html'
    form_class = LoginForm
    success_url = 'mypage/'

    def form_valid(self, form):
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authentication_classes.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/success/')
            else:
                return render(request, 'users/sign_in2.html', {'error':'username or password is incorrect'})
            # 로그인 실패시 'username or password is incorrect' 메시지를 띄움  
        else:
            return render(request, 'users/sign_in2.html')
    #     self.request.session['user'] = form.data.get('email')
    #     return super().form_valid(form)

# class PasswordResetView(FormView):


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

@api_view(['GET'])
def userAPI(request):
    userlist = list(Users.objects.all())
    serializer = UserSerializer(userlist, many=True)
    return Response(serializer.data)


def send_email(): 
    subject = "메시지" 
    to = ['aaa@bbb.com'] 
    from_email = 'myaccount@gmail.com' 
    message = "메시지를 성공적으로 전송" 
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()


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
            redirect_url = "http://127.0.0.1:8000/share/twitter/"
            return HttpResponseRedirect(redirect_url)
        except ConnectionError:
            return HttpResponse(
                "<html><body>You have no internet connection</body></html>", status=403
            )

        except:
            return HttpResponse(
                "<html><body>Something went wrong.Try again.</body></html>", status=403
            )

def TwitterShare(request):
    search_words = ["#krishian_1_0_0"]
    tweet_info = tweet_scrap(search_words)
    data_text = "3,5,7,10,0.5,0.80,1.20,1.60,1.40,5.6,5.8,6,18,12,65,75,50,70,5,10,400,21,5 "

    content = {
        "tweet_info": tweet_info,
        "data_text": data_text,
    }
    return render(request, 'twitter.html', content)