from django.contrib import admin
from django.urls import path
from users.views import home, signUp
from users.views import LoginView, RegisterView, userAPI
from . import views
urlpatterns = [
    path('', home),
    path('signin/', views.signIn, name='signIn'),

    path('signup/', views.signUp, name='signUp'),
    path('login/', LoginView.as_view(), name='LoginView'),
    path('register/', RegisterView.as_view(), name='RegisterView'),
    path('userlist/',userAPI)
]