from django.urls import path

from product.views import *

urlpatterns = [
    path('', get_products),
    path('<int:product_id>/', get_product),
    path('create/', create_product),
    path('<int:product_id>/delete/', delete_product),
]