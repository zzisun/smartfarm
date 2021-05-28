from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
from .models import Device_Info, Farm_Info, Growth_Params
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import POST_Growth_Param_Serializer, POST_Mock, POST_Farm_Info
import json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def control(request):
    return render(request, 'device_management/control.html')


# has to fix when Device data is exist, move to control.html, not exists, move to device1.html
# In this time, just get data from html3, device_serial, device_name.
def device(request):
    device_name = request.GET.get("device_name")
    device_serial = request.GET.get("device_serial")
    device_model = request.GET.get("modelno")
    device_detail = request.GET.get("detail")
    device_ip_address = request.GET.get("ip_address")
    device_password = request.GET.get("password")

    print("name=id =" + device_name, device_serial, device_ip_address, "password : "+ device_password)
    device_information = Device_Info.objects.all()
    

    try :
        device_information = Device_Info(device_serial = request.GET.get("device_serial"), \
            device_detail = request.GET.get("detail"), \
            device_model = request.GET.get("modelno"), \
            device_name = request.GET.get("device_name"),\
            device_ip_address = request.GET.get("ip_address"), \
            device_password = request.GET.get("password"))
        device_information.save()
    except Exception as ex:
        device_information  = None
        print("EXCEPTION----------------------------device_info store", ex)

    context = {'device_info': device_information} #send information to html file!
    return render(request, 'device_management/device4.html', context = context)

def device1(request):
    return render(request, 'device_management/device1.html')

def device2(request):
    return render(request, 'device_management/device2.html')

def device3(request):
    return render(request, 'device_management/device3.html')

def device4(request):
    
    
    return render(request, 'device_management/device4.html')

def device7(request):
    #device_info_serial = request.POST['device_info'].get("device_serial")
    
    device_serial = request.POST.get('device_serial') #changed way to send and receive only device_serial value not device_info object
    #context = {'device_serial': device_info_serial} #send information to html file!

    
    context = {'device_serial': device_serial}
    print(device_serial)
    return render(request, 'device_management/device7.html', context=context)

def farm_info_setting(request):
    mock_farm_info = {
        "device_info"
    }

class create_farm_info(APIView):
    def post(self, request):
        serializer = POST_Farm_Info(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class create_plant_params(APIView):

    def post(self, request):
        serializer = POST_Mock(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    
