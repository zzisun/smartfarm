from .models import Growth_Params, mock_params, Farm_Info,  Device_Info, Plant_Info
from rest_framework import serializers

class POST_Growth_Param_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Growth_Params
        fields = '__all__'

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