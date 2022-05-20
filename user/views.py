from django.contrib.auth import authenticate, tokens
from django.contrib.auth import login as dj_login
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import CustomUser
from user.serializers import UserSerializer


class Login(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = UserSerializer(data=request.data).initial_data
        user = authenticate(request, username=user.get("username"), password=user.get("password"))
        if user:
            refresh = RefreshToken.for_user(user)
            tokens.default_token_generator.algorithm()
            dj_login(request, user)
            return Response(
                {
                    'success': True,
                    'tokens': str(),
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            )
        return Response({"success": False})


class Register(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        UserSerializer(data=request.data).create(request.data)
        return Response({'success': True})


class GetUsers(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        users = CustomUser.objects.all()
        return Response(UserSerializer(users, many=True).data)

