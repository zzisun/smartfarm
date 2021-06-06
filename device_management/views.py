from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
from .models import Device_Info, Farm_Info, Growth_Params, Plant_Info
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import POST_Growth_Param_Serializer, POST_Mock, POST_Farm_Info, POST_Plant_Info
from users.models import Users
from django.utils import timezone
from .forms import Growth_Params_Form

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

    
