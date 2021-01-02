from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser, Commodity
from django.contrib.auth.models import User
from .serializers import CustomUserSerializer, UserSerializer, CommoditySerializer
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet

# user api
class UserView(ObjectMultipleModelAPIViewSet):
	pagination_class = None
	querylist = [
		{'queryset' : CustomUser.objects.all(), 'serializer_class': CustomUserSerializer},
		{'queryset' : User.objects.all(), 'serializer_class': UserSerializer},
	]

# commodity api
class CommodityView(viewsets.ModelViewSet):
	queryset = Commodity.objects.all()
	serializer_class = CommoditySerializer

