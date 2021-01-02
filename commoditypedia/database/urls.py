from django.urls import path, include
from . import views
from rest_framework import routers

# user api
simple_router = routers.SimpleRouter()
simple_router.register('custom_user_api', views.UserView, basename='user')
# commodity api
default_router = routers.DefaultRouter()
default_router.register('commodity_api', views.CommodityView)

urlpatterns = [
	path('/', include(simple_router.urls)),
	path('/', include(default_router.urls)),
]