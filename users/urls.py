from django.contrib import admin
from django.urls import path

from users.views import home, registerPage, signUp, success

from django.contrib.auth import views as auth_views
from . import views
from users.views import LoginView, RegisterView, userAPI, TwitterAuthRedirectEndpoint, TwitterCallbackEndpoint, TwitterShare

urlpatterns = [
    path('', home, name='home'),
    path('', views.home, name='home'),
    path('mypage/', views.mypage, name='mypage'),
    path('signup/', views.registerPage, name='signup'),
    path('verify/',views.verifyAccount, name='verify'),
    path('login/', views.loginPage, name='login'),
    path('success/', views.success, name='success'),
    path('mypage/', views.mypage, name='mypage'),

    # path('signup/', views.registerPage, name='registerPage'),
    # path('login/', LoginView.as_view(), name='LoginView'),

    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('createPassword/', views.createPassword, name='createPassword'),
    # path('signup/', RegisterView.as_view(), name='RegisterView'),
    path('userlist/',userAPI),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path('register/', RegisterView.as_view(), name='RegisterView'),
    path('userlist/',userAPI),
    path("auth/twitter/redirect/", TwitterAuthRedirectEndpoint.as_view(), name="twitter-login-redirect"),
    path("callback/twitter/", TwitterCallbackEndpoint.as_view(), name="twitter-login-callback"),
    path("share/twitter/", TwitterShare, name="twitter-share")
]