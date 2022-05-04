from django.urls import path

from product import views

urlpatterns = [
    path('', views.ProductsApi.as_view()),
    path('<int:product_id>/', views.ProductApi.as_view()),
    path('create/', views.ProductApi.as_view()),
    path('<int:product_id>/delete/', views.ProductApi.as_view()),
]