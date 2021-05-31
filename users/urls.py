from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from users.views import userAPI, TwitterAuthRedirectEndpoint, TwitterCallbackEndpoint, TwitterShare

urlpatterns = [
    path('', views.home, name='home'),
    path('mypage/', views.mypage, name='mypage'),
    path('signup/', views.registerPage, name='signup'),
    path('verify/',views.verifyAccount, name='verify'),
    path('login/', views.loginPage, name='login'),
    path('success/', views.success, name='success'),
    path('mypage/', views.mypage, name='mypage'),

    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('createPassword/', views.createPassword, name='createPassword'),
    path('userlist/',userAPI),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path('userlist/',userAPI),
    path("auth/twitter/redirect/", TwitterAuthRedirectEndpoint.as_view(), name="twitter-login-redirect"),
    path("callback/twitter/", TwitterCallbackEndpoint.as_view(), name="twitter-login-callback"),
    path("share/twitter/", TwitterShare, name="twitter-share")
]