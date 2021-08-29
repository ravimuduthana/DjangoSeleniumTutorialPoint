from rest_framework import serializers
from Home.models import Users

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Users
        fields='__all__'