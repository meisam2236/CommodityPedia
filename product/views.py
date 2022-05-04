from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import *
from product.serializers import ProductSerializer


@api_view(['POST'])
def create_product(request):
    ProductSerializer(data=request.data).create(request.data)
    return Response({'status': 'Product created'})


@api_view(['GET'])
def get_products(request):
    products = list()
    for product in Product.objects.all():
        products.append(ProductSerializer(product).data)
    return Response(products)


@api_view(['GET'])
def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return Response(ProductSerializer(product).data)


@api_view(['DELETE'])
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return Response({'status': 'Product deleted'})
