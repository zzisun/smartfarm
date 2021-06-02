"""plog_dm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

app_name = "device_management"

urlpatterns = [
    path('', views.device1, name='device1'),
    path('control',views.control, name='control'),
    path('device',views.device, name='device'),
    path('device1', views.device1, name='device1'),
    path('device2', views.device2, name='device2'),
    path('device3', views.device3, name='device3'),
    path('device4', views.device4, name='device4'),
    path('device7', views.device7, name='device7'),
    path('create_plant_params', views.create_plant_params.as_view(), name='create_plant_params'),
    path('create_farm_info', views.create_farm_info.as_view(), name='Create_farm_info'),
    path('crop_info_registeration', views.crop_info_registeration.as_view(), name='crop_info_registeration'),
    path('status', views.status, name='status'),
    path('history_detail',views.history_detail, name='history_detail'),
]
