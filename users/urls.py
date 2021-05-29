from django.contrib import admin
from django.urls import path
from users.views import home
from users.views import LoginView, RegisterView, userAPI, TwitterAuthRedirectEndpoint, TwitterCallbackEndpoint
urlpatterns = [
    path('', home),
    path('login/', LoginView.as_view(), name='LoginView'),
    path('register/', RegisterView.as_view(), name='RegisterView'),
    path('userlist/',userAPI),
    path("auth/twitter/redirect/", TwitterAuthRedirectEndpoint.as_view(), name="twitter-login-redirect"),
    path("callback/twitter/", TwitterCallbackEndpoint.as_view(), name="twitter-login-callback"),
]