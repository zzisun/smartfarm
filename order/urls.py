from django.urls import path

from .views import OrderCreate

urlpatterns = [
    path('create/', OrderCreate.as_view()),
    path('complete/',OrderCreate.as_view(), name='ordercomplete'),
]