from .models import Growth_Params, mock_params
from rest_framework import serializers

class POST_Growth_Param_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Growth_Params
        fields = '__all__'

class POST_Mock(serializers.ModelSerializer):
    class Meta :
        model = mock_params
        fields = '__all__'