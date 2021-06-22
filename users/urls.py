from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from users.views import userAPI, TwitterAuthRedirectEndpoint, TwitterCallbackEndpoint

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),

    path('signup/', views.registerPage, name='signup'),
    path('verify/',views.verifyAccount, name='verify'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('success/', views.success, name='success'),
    path('mypage/', views.mypage, name='mypage'),

    path('profile/', views.edit_profile, name='profile'),
    path('billingInfo/', views.billing_info, name='billingInfo'),
    path('change_password/',views.change_password, name='change_password'),
     
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
     name="reset_password"),
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_sent.html"), 
        name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_form.html"), 
     name="password_reset_confirm"),
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_done.html"), 
        name="password_reset_complete"),

    path('userlist/',userAPI),
    path("auth/twitter/redirect/", TwitterAuthRedirectEndpoint.as_view(), name="twitter-login-redirect"),
    path("callback/twitter/", TwitterCallbackEndpoint.as_view(), name="twitter-login-callback"),
]
