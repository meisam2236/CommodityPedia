from rest_framework import serializers
from .models import CustomUser, Commodity
from django.contrib.auth.models import User

class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User 
		fields = ('id', 'last_login', 'username', 'email', 'is_active', 'date_joined')

class CommoditySerializer(serializers.ModelSerializer):
	class Meta:
		model = Commodity
		fields = '__all__'
		depth = 1
