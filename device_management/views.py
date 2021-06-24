from functools import partial
from django.http.response import Http404
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.core import serializers
from rest_framework.serializers import Serializer
# Create your views here.

from .models import Default_Status, Device_Info, Farm_Info, Growth_Params, Plant_Info, mock_params, Device_Interface 
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Default_Status_Serializer, GET_MOCK_Interface, POST_Growth_Param_Serializer, POST_Mock, POST_Farm_Info, POST_Plant_Info, Serial_Interface
from .forms import Farm_Info_Form,Growth_Params_Form
import json
from django.views.decorators.csrf import csrf_exempt
from .status_default import Status_Default
#from .handling_excel import Default_Status_Handler


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
                                                             'grow_param': grow_param,
                                                             'device_info': device_info})

def mypage_status(request):
    return render(request, 'device_management/mypage.html')


def history_detail(request, device_serial, farm_id, plant_id):
    '''
    if request.method == 'GET':
        device_serial = request.GET['device_info']
    ''' 
    
    status = get_mock_plant_status.get(get_mock_plant_status, request, device_serial, plant_id)
    #print(status.data)
    farm_info = Farm_Info.objects.get(pk=farm_id)
    plant_info = Plant_Info.objects.get(pk = plant_id)
    device_info = Device_Info.objects.get(pk = device_serial)

    return render(request, 'device_management/history_detail.html', {"status":status.data, "device_info":device_info,\
        "farm_info":farm_info, "plant_info":plant_info })



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
        status = serializers.serialize('json',Growth_Params.objects.filter(deivce_info = device_serial).order_by('date'))
        print(status)

        context = {'status':status, 'farm':farm_info_inst, 'plant':plant_information}

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
        serializer = POST_Growth_Param_Serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)





class get_mock_plant_status(APIView):

    def get_object(self, info):
        try:
            device_serial = info['device_info']
            plant_info = info['plant_info']
            date = info['date']
            growth_param_obj = Growth_Params.objects.filter(device_info = (device_serial)).filter(plant_info = plant_info).filter(date=date)
            if len(growth_param_obj) >= 1:
                return growth_param_obj[len(growth_param_obj)-1]
        except Growth_Params.DoesNotExist:
            print(Growth_Params.DoesNotExist)
            return -1

    def get(self, request, device_serial, plant_id):
        status_saved = Growth_Params.objects.filter(device_info = str(device_serial)).filter(plant_info = plant_id).order_by('-date')[:10]
        status_serialized = serializers.serialize('json',status_saved)

        if status_serialized:
            #return render(request, 'device_management/history_detail.html', {"status":status_serialized})
            return Response(status_serialized, status=200)
        return Response(status_serialized, status=400)

    def post(self, request):
        
        json_Req_body = json.loads(request.body)
        info = dict(device_info = json_Req_body['device_info'], plant_info = json_Req_body['plant_info'], date = json_Req_body['date'])
        
        growth_status = self.get_object(info)
        if growth_status == -1:
            growth_status_serialized = POST_Growth_Param_Serializer(data = json_Req_body)

        growth_status_serialized = POST_Growth_Param_Serializer(growth_status, data=json_Req_body, partial=True)
        
        if growth_status_serialized.is_valid():
            #print(growth_status_serialized.data)
            growth_status_serialized.save()
            return Response(growth_status_serialized.data, status=200)
        return Response(growth_status_serialized.errors, status=400)


class GET_Interface_To_Device_Manual(APIView):

    def get_object(self, device_info):
        try: 
            interface_obj = Device_Interface.objects.get(device_info = device_info)
            return interface_obj
        except Device_Interface.DoesNotExist:
            print(Device_Interface.DoesNotExist)
            return -1

    def post(self, request):
        
        #why can't i get value with key "device_info" when use request.POST['device_info'] ??????????
        print(int(request.data['device_info']))
        catch_interface = self.get_object(device_info = int(request.data['device_info']))

        if catch_interface == -1: #foolish but, we should make new instance for Interface...
            interface_serializer = Serial_Interface(data = request.data)
        else:
            interface_serializer = Serial_Interface(catch_interface, data = request.data)

        if interface_serializer.is_valid():
            if interface_serializer.validated_data['nut_pump_auto'] == 1:
                print("nutrient automode activated")
            else:
                print("nutrient automode de-activated")
            
            if interface_serializer.validated_data['water_pump_auto'] == 1:
                print("water-pump automode activated")
            else:
                print("water-pump automode de-activated")
            
            if interface_serializer.validated_data['oxy_pump_auto'] == 1:
                print("oxygen automode activated")
            else:
                print("oxygen automode de-activated")

            if interface_serializer.validated_data['auto_air_contiditon_pump'] == 1:
                print("air condition automode activated")
            else:
                print("air condition automode de-activated")
            
            interface_serializer.save()

            return Response(interface_serializer.data, status=200)
        return Response(interface_serializer.errors, status=400)


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

    device_ip = Device_Info.objects.get(pk = device_serial).device_ip_address
    farm_info_inst = Farm_Info.objects.get(pk=int(farm_info_id))
    crop_name = Plant_Info.objects.get(farm_info_id = int(farm_info_id)).crop_name
    plant_id = Plant_Info.objects.get(farm_info_id = int(farm_info_id)).id

    context = {'device_serial':device_serial, "farm_info":farm_info_inst, "crop_name":crop_name, "device_ip" : device_ip, "plant_id" : plant_id}
    return render(request, "device_management/control.html", context)



class compare_currentState_with_default(APIView):
    def post(self,request):

        default_temp = {'min':55, 'max':75}
        default_ph = {'min':6.0, 'max':7.5}
        default_ec = {'min':0.8, 'max':1.2}
        default_humidity = {'min':50, 'max':70}
        default_do = {'min':5, 'max':8}
        default_co2 = {'min':400, 'max':410}
        default_light_hr = {'min':12, 'max':18}

        diff_co2 = 0
        diff_do = 0
        diff_ec = 0
        diff_humidity = 0
        diff_ph = 0
        diff_light_hr = 0
        diff_temp = 0 

        '''
        req_json = json.loads(request.body)
        device_info = req_json['device_info']
        plant_info = req_json['plant_id']
'''

        device_info = request.data['device_info']
        plant_info = request.data['plant_id']

        
        latest_status = Growth_Params.objects.filter(device_info = device_info).filter(plant_info = plant_info).order_by('-date')[0]
        print(latest_status.date)

        this_crop_name = Plant_Info.objects.get(id = plant_info).crop_name
        print("crop name is : "+ this_crop_name)
        default_status = Default_Status.objects.get(crop_name = this_crop_name)
        
        '''
        if latest_status.temparature < default_temp["min"]:
            diff_temp = latest_status.temparature - default_temp["min"]
        elif latest_status.temparature > default_temp["max"]:
            diff_temp = latest_status.temparature - default_temp['max']
        
        if latest_status.ph < default_ph["min"]:
            diff_ph = latest_status.ph - default_ph["min"]
        elif latest_status.ph > default_ph["max"]:
            diff_ph = latest_status.ph - default_ph['max']

        if latest_status.ec < default_ec["min"]:
            diff_ec = latest_status.ec - default_ec["min"]
        elif latest_status.ec > default_ec["max"]:
            diff_ec = latest_status.ec - default_ec['max']

        if latest_status.humidity < default_humidity["min"]:
            diff_humidity = latest_status.humidity - default_humidity["min"]
        elif latest_status.humidity > default_humidity["max"]:
            diff_humidity = latest_status.humidity - default_humidity['max']

        if latest_status.do < default_do["min"]:
            diff_do = latest_status.do - default_do["min"]
        elif latest_status.do > default_do["max"]:
            diff_do = latest_status.do - default_do['max']

        if latest_status.co2 < default_co2["min"]:
            diff_co2 = latest_status.co2 - default_co2["min"]
        elif latest_status.co2 > default_co2["max"]:
            diff_co2 = latest_status.co2 - default_co2['max']

        if latest_status.light_hr < default_light_hr["min"]:
            diff_light_hr = latest_status.light_hr - default_light_hr["min"]
        elif latest_status.light_hr > default_light_hr["max"]:
            diff_light_hr = latest_status.light_hr - default_light_hr['max']
        '''

        if latest_status.temparature < default_status.temp_min:
            diff_temp = latest_status.temparature - default_status.temp_min
        elif latest_status.temparature > default_status.temp_max:
            diff_temp = latest_status.temparature - default_status.temp_max
        
        if latest_status.ph < default_status.ph_min:
            diff_ph = latest_status.ph - default_status.ph_min
        elif latest_status.ph > default_status.ph_max:
            diff_ph = latest_status.ph - default_status.ph_max

        if latest_status.ec < default_status.ec_min:
            diff_ec = latest_status.ec - default_status.ec_min
        elif latest_status.ec > default_status.ec_max:
            diff_ec = latest_status.ec - default_status.ec_max

        if latest_status.humidity < default_status.humidity_min:
            diff_humidity = latest_status.humidity - default_status.humidity_min
        elif latest_status.humidity > default_status.humidity_max:
            diff_humidity = latest_status.humidity - default_status.humidity_max

        if latest_status.do < default_status.do_min:
            diff_do = latest_status.do - default_status.do_min
        elif latest_status.do > default_status.do_max:
            diff_do = latest_status.do - default_status.do_max

        if latest_status.co2 < default_status.co2_min:
            diff_co2 = latest_status.co2 - default_status.co2_min
        elif latest_status.co2 > default_status.co2_max:
            diff_co2 = latest_status.co2 - default_status.co2_max

        if latest_status.light_hr < default_status.light_hr_min:
            diff_light_hr = latest_status.light_hr - default_status.light_hr_min
        elif latest_status.light_hr > default_status.light_hr_max:
            diff_light_hr = latest_status.light_hr - default_status.light_hr_max

        context = {
            'diff_light_hr' : diff_light_hr,
            'diff_do' : round(diff_do,1),
            'diff_co2' : diff_co2,
            'diff_ec' : round(diff_ec,1),
            'diff_humidity' : round(diff_humidity,1),
            'diff_temp' : diff_temp,
            'diff_ph' : round(diff_ph,1)
        }
        return Response(context, status=200)

    

class Store_Default_Status(APIView):
    def put(self, request):
        print(request.data)
        serializer = Default_Status_Serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
        