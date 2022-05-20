from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from user.views import Login, Register, GetUsers

urlpatterns = [
    path('login/', Login.as_view()),
    path('register/', Register.as_view()),
    path('', GetUsers.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
