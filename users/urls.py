from django.contrib import admin
from django.urls import path
from users.views import home
from users.views import LoginView, RegisterView, userAPI
from . import views
urlpatterns = [
    path('', views.signIn, name='signIn'),
    # path('', home),
    path('login/', LoginView.as_view(), name='LoginView'),
    path('register/', RegisterView.as_view(), name='RegisterView'),
    path('userlist/',userAPI)
]