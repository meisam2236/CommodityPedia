from django.contrib.auth import authenticate, login as dj_login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.models import CustomUser
from user.serializers import UserSerializer


@csrf_exempt
@api_view(['POST'])
def login(request):
    user = UserSerializer(data=request.data).initial_data
    user = authenticate(request, username=user.get("username"), password=user.get("password"))
    if user:
        dj_login(request, user)
        return Response({'success': True})
    return Response({'success': False})


@csrf_exempt
@api_view(['POST'])
def register(request):
    UserSerializer(data=request.data).create(request.data)
    return Response({'success': True})


@csrf_exempt
@api_view(['GET'])
def get_users(request):
    users = CustomUser.objects.all()
    return Response(UserSerializer(users, many=True).data)
