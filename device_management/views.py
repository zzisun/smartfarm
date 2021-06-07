from datetime import timezone
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core import serializers
from rest_framework.serializers import Serializer
# Create your views here.

from .models import Device_Info, Farm_Info, Growth_Params, Plant_Info, mock_params
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GET_MOCK_Interface, POST_Growth_Param_Serializer, POST_Mock, POST_Farm_Info, POST_Plant_Info
from .forms import Farm_Info_Form,Growth_Params_Form
import json
from django.views.decorators.csrf import csrf_exempt
from .status_default import Status_Default



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def control(request):
    return render(request, 'device_management/control.html')

def mypage(request):
    user = request.user
    try:
        device_info = Device_Info.objects.filter(device_user=user)[0]
    except:
        return redirect('device_management:device1')
    print(device_info)
    farm_list = Farm_Info.objects.filter(device_info=device_info)
    print(farm_list)
    farm_dict = {}
    for farm in farm_list:
        plant = Plant_Info.objects.get(farm_info=farm)
        grow_param = Growth_Params.objects.filter(plant_info=plant)
        if grow_param:
            farm_dict[farm] = grow_param[len(grow_param)-1]#not allow negative indexing
        else:
            farm_dict[farm] = None
    print(farm_dict)
    return render(request, 'device_management/mypage.html', {'farm_list': farm_dict})

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
        device_information = None
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

def device6(request):
    return render(request, 'device_management/device6.html')



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

def status(request, pk):
    device_info = Device_Info.objects.filter(device_user=request.user)[0]
    farm = Farm_Info.objects.get(id=pk)
    plant = Plant_Info.objects.get(farm_info=farm)
    grow_param = Growth_Params.objects.filter(plant_info=plant)
    if request.method == 'POST':
        form = Growth_Params_Form(request.POST)
        if form.is_valid():
            param = form.save(commit=False)
            param.device_info = device_info
            param.plant_info = plant
            param.date = timezone.now()
            param.save()
            print(param)
        #Growth_Params.objects.create(
        #    device_info = device_info,
        #    plant_info = plant,#already exist data
        #    germination_time = request.data["germination_time"],
        #    seeding_ec = request.data["seeding_ec"],
        #    ec = request.data["ec"],
        #    progress_date=request.data["progress_date"],
        #    temparature=request.data["temparature"],
        #    ph=request.data["ph"],
        #    humidity=request.data["humidity"],
        #    date=timezone.now(),#already exist
        #    light_hr=request.data["light_hr"],
        #)
    if grow_param:
        grow_param = grow_param[len(grow_param) - 1]
    else:
        grow_param = None
    return render(request, 'device_management/status.html', {'farm':farm,
                                                             'plant':plant,
                                                             'grow_param': grow_param})

def mypage_status(request):
    return render(request, 'device_management/mypage.html')


def history_detail(request):
    '''
    if request.method == 'GET':
        device_serial = request.GET['device_info']
'''
    return render(request, 'device_management/history_detail.html')

class crop_info_registeration(APIView):
    def post(self, request):
        print(request.data)
        crop_serializer = POST_Plant_Info(data = request.data)
        
        if crop_serializer.is_valid():
            crop_serializer.save()
            crop_id = crop_serializer.data["id"]
            crop_info = Plant_Info.objects.get(id=crop_id)
            return redirect('device_management:status', pk=request.data["farm_info"])
        return Response(crop_serializer.errors, status=400)


@csrf_exempt
def crop_info_reg_f(request):
    if request.method == 'POST':
        farm_info_id = int(request.POST['farm_info'])
        print(farm_info_id)
        farm_info_inst = Farm_Info.objects.get(pk=farm_info_id)
        print(farm_info_inst.farm_name)
        crop_group = request.POST['crop_group']
        crop_name = request.POST['crop_name']
        life_stage = request.POST['life_stage']
        planting_date = request.POST['planting_date']

    elif request.method == 'GET':
        farm_info_id = int(request.GET.get('farm_info'))
        print(farm_info_id)
        farm_info_inst = Farm_Info.objects.get(pk=farm_info_id)
        crop_group = request.GET.get('crop_group')
        crop_name = request.GET.get('crop_name')
        life_stage = request.GET.get('life_stage')
        planting_date = request.GET.get('planting_date')

    print("plant info: "+crop_group, crop_name,life_stage,planting_date)
    plant_information = Plant_Info.objects.all()
    
    try :
        plant_information = Plant_Info(farm_info = farm_info_inst, \
            crop_group =crop_group , \
            crop_name = crop_name, \
            life_stage = life_stage,\
            planting_date = planting_date, \
            )
        plant_information.save()

        device_serial = farm_info_inst.device_info_id
 

        # filter method returns "QuerySet" object, so Must serialize using from django.core import serializers.serialize()
        # Structure is not normal json, like this
        '''
        {"model": "device_management.mock_params", "pk": 11, "fields": {{"serial": "22222222", "ph": 5.0, "temp": 53, ...+}
        '''
        mock_status = serializers.serialize('json',mock_params.objects.filter(serial = str(device_serial)).order_by('date'))
        print(mock_status)

        context = {'mock_status':mock_status, 'farm':farm_info_inst, 'plant_info_inst':plant_information}

        return render(request, "device_management/status.html", context=context) 
    except Exception as ex:
        plant_information = None
        print("EXCEPTION----------------------------plant_information store", ex)
        return HttpResponse(content = ex)
           

class create_farm_info(APIView):
   def post(self, request):
        print(request.data)
        serializer = POST_Farm_Info(data = request.data)

        if serializer.is_valid():
            serializer.save()

            farm_info = serializer.data["id"]
            #farm_info_name = Farm_Info.objects.get(farm_name = farm_info).farm_name
            context = {'farm_info':farm_info}
            return render(request, 'device_management/device6.html',context = context)

        else:
            print(serializer.data)
            return Response(serializer.errors, status=400)


'''
class create_farm_info(APIView):
    def post(self, request):
        if request.method == 'POST':
            farm_form = Farm_Info_Form(request.POST)
            if farm_form.is_valid():
                device = farm_form.cleaned_data['device_info'].device_serial
                farm_save = farm_form.save()
                farm_save.save()
                farm_info_pk = Farm_Info.objects.get(device_info = device).id
                return render(request, 'device_management/device6.html',{'farm_info':farm_info_pk}) 
'''

class create_plant_params(APIView):

    def post(self, request):
        serializer = POST_Mock(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class get_mock_plant_status(APIView):

    def get(self, request, serial):
        status_saved = mock_params.objects.filter(serial = str(serial)).order_by('date')
        status_serialized = serializers.serialize('json',status_saved)

        if status_serialized:
            return render(request, 'device_management/history_detail.html', {"status":status_serialized})
        return Response(status_serialized, status=400)


class GET_Interface_To_Device_Manual(APIView):
    def get(self, request):
        interface_manual_serializer = GET_MOCK_Interface(data = request.data)

        if interface_manual_serializer.is_valid():
            return Response(interface_manual_serializer.data, status=200)
        return Response(interface_manual_serializer.errors, status=400)



# sending data with address, you should add parameter of function, cannot get with request.GET
def goto_control_device(request, device_serial, farm_id):
    if request.method == 'GET':
        #device_serial = request.GET.get('device_serial')
        #farm_info_id = request.GET.get('farm_id')
        device_serial = device_serial
        farm_info_id = farm_id

    if request.method == 'POST':
        device_serial = request.POST['device_serial']
        farm_info_id = request.POST['farm_id']

    print("url requests")
    print(device_serial, farm_info_id)

    farm_info_inst = Farm_Info.objects.get(pk=int(farm_info_id))
    crop_name = Plant_Info.objects.get(farm_info_id = int(farm_info_id)).crop_name

    context = {'device_serial':device_serial, "farm_info":farm_info_inst, "crop_name":crop_name}
    return render(request, "device_management/control.html", context)