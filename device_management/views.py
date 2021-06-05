from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
from .models import Device_Info, Farm_Info, Growth_Params, Plant_Info
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import POST_Growth_Param_Serializer, POST_Mock, POST_Farm_Info, POST_Plant_Info
from users.models import Users

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def control(request):
    return render(request, 'device_management/control.html')

def mypage(request):
    user = request.user
    device_info = Device_Info.objects.filter(device_user=user)[0]
    print(device_info)
    farm_list = Farm_Info.objects.filter(device_info=device_info)
    print(farm_list)
    return render(request, 'device_management/mypage.html', {'farm_list': farm_list})

# has to fix when Device data is exist, move to control.html, not exists, move to device1.html
# In this time, just get data from html3, device_serial, device_name.
def device(request):
    device_information = Device_Info.objects.all()
    print(request.user)
    print(device_information)
    try :
        device_information = Device_Info.objects.create(
            device_user = request.user,
            device_serial = request.GET.get("device_serial"), \
            device_detail = request.GET.get("detail"), \
            device_model = request.GET.get("modelno"), \
            device_name = request.GET.get("device_name"),\
            device_ip_address = request.GET.get("ip_address"), \
            device_password = request.GET.get("password"))
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
    try:
        device_info = Device_Info.objects.filter(device_user=request.user)[0]
        return render(request, 'device_management/device4.html', {'device_info': device_info})
    except:
        return redirect('device_management:device1')




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

def status(request):
    return render(request, 'device_management/status.html')

class crop_info_registeration(APIView):
    def post(self, request):
        print(request.data)
        crop_serializer = POST_Plant_Info(data = request.data)
        
        if crop_serializer.is_valid():
            crop_serializer.save()
            crop_id = crop_serializer.data["id"]
            crop_info = Plant_Info.objects.get(id=crop_id)
            return render(request, 'device_management/status.html', {'crop_info': crop_info})
        return Response(crop_serializer.errors, status=400)


class create_farm_info(APIView):
   def post(self, request):
        print(request.data)
        serializer = POST_Farm_Info(data = request.data)

        if serializer.is_valid():
            serializer.save()
            farm_info = serializer.data["farm_name"]
            print("farm info : ", farm_info)
            farm_info_name = Farm_Info.objects.get(farm_name = farm_info)
            print("farm id : ", farm_info_name)
            return render(request, 'device_management/device6.html',{'farm_info':farm_info_name})
        else:
            print(serializer.data)
            return Response(serializer.errors, status=400)

class create_plant_params(APIView):

    def post(self, request):
        serializer = POST_Mock(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    
