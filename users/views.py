from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from users.models import Users
from .form import RegisterForm, LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer

# for OAuth in twitter
# from requests_oauthlib import OAuth1
from urllib.parse import urlencode
from rest_framework.views import APIView
from django.http.response import HttpResponseRedirect, HttpResponse
from django.conf import settings

import requests


def home(request):
    return render(request, 'home.html', {'user' : request.session.get('user')})


class RegisterView(FormView):
    template_name = 'user_register.html'
    form_class = RegisterForm
    success_url = '/login'

    def form_valid(self, form):
        user = Users(
            email=form.data.get('email'),
            name=form.data.get('name'),
            password=make_password(form.data.get('password')),
            level='user'
        )
        user.save()

        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/product'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')
        return super().form_valid(form)


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

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
            redirect_url = "http://127.0.0.1:8000/twitter/share/"
            return HttpResponseRedirect(redirect_url)
        except ConnectionError:
            return HttpResponse(
                "<html><body>You have no internet connection</body></html>", status=403
            )

        except:
            return HttpResponse(
                "<html><body>Something went wrong.Try again.</body></html>", status=403
            )

