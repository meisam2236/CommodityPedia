from django.contrib.auth import authenticate, login as dj_login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
