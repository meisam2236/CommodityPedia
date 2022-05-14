from django.contrib.auth import authenticate, login as dj_login
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import CustomUser
from user.serializers import UserSerializer

#
# @swagger_auto_schema(method='post', request_body=openapi.Schema(
#     type=openapi.TYPE_OBJECT,
#     properties={
#         'username': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
#         'password': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
#     }
# ))
@csrf_exempt
@api_view(['POST'])
def login(request):

    user = UserSerializer(data=request.data).initial_data
    user = authenticate(request, username=user.get("username"), password=user.get("password"))
    refresh = RefreshToken.for_user(user)

    if user:
        dj_login(request, user)
        return Response(
            {
                'success': True,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        )
    return Response({"success": False})


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
