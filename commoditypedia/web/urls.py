from django.urls import path, include
from . import views

app_name = 'web'

urlpatterns = [
	path('', views.home, name='home'),
	path('home', views.home, name='home_address'),

	path('profile', views.profile, name='profile'),

	path('sign_in', views.sign_in, name='sign_in'),
	path('sign_in/login/', views.login, name='login'),

	path('sign_up/', views.sign_up, name='sign_up'),
	path('sign_up/register/', views.register, name='register'),

	path('log_out', views.log_out, name='log_out'),

	path('forget_pass', views.forget_pass, name='forget_pass'),

	path('add', views.add, name='add'),

	path('search', views.search, name='search'),

	path('user_infos', views.user_infos, name='user_infos'),

	path('like/<int:pk>/', views.like, name='like_stuff'),
	path('comment/<int:pk>/', views.comment, name='comment_stuff'),
	path('search_user', views.search_user, name='search_user'),
	path('search_commodity', views.search_commodity, name='search_commodity'),
]
