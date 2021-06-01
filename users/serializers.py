from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        # Users에서 name 속성이 삭제되어 다음과 같이 수정하였습니다.
        fields =  ('email', 'first_name', 'last_name')