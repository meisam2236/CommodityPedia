from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import *
from product.serializers import ProductSerializer


class ProductApi(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        return Response(ProductSerializer(product).data)

    def post(self, request):
        ProductSerializer(data=request.data).create(request.data)
        return Response({'status': 'Product created'})

    def delete(self, request, product_id):
        product = Product.objects.get(id=product_id)
        product.delete()
        return Response({'status': 'Product deleted'})


class ProductsApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        products = list()
        for product in Product.objects.all():
            products.append(ProductSerializer(product).data)
        return Response(products)
