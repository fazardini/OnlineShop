from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from shopping.models import Product
from shopping.permissions import IsProductCreator
from shopping.serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        method = self.request.method
        if method == 'GET':
            return [AllowAny()]
        else:
            return [IsAdminUser()]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteProduct(generics.DestroyAPIView):
    permission_classes = [IsProductCreator]
    queryset = Product.objects.filter(sales_number=0)
