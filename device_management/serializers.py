from .models import Default_Status, Growth_Params, mock_params, Farm_Info,  Device_Info, Plant_Info, mock_interface, Device_Interface, \
    Default_Status
from rest_framework import serializers

class POST_Growth_Param_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Growth_Params
        fields = '__all__'
    def create(self, validated_data):
        return Growth_Params.objects.create(**validated_data)
    

class POST_Mock(serializers.ModelSerializer):
    class Meta :
        model = mock_params
        fields = '__all__'

class POST_Farm_Info(serializers.ModelSerializer):
    class Meta :
        model = Farm_Info
        fields = '__all__'

class POST_Plant_Info(serializers.ModelSerializer):
    class Meta : 
        model = Plant_Info
        fields = '__all__'

''' do not use anymore... '''
class GET_MOCK_Interface(serializers.ModelSerializer):
    class Meta : 
        model = mock_interface
        fields = ['device_info', 'cooler', 'humidifier', 'co2_gen', 'air_pump']

class Serial_Interface(serializers.ModelSerializer):
    class Meta : 
        model = Device_Interface
        fields = "__all__"


class Default_Status_Serializer(serializers.ModelSerializer):
    class Meta :
        model = Default_Status
        fields = "__all__"
        exclude = []
        