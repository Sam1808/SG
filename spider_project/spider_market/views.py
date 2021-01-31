from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework.views import APIView
from .serializers import UserRegisterSerializer, CategorySerializer, CompanySerializer, ProductSerializer

from .models import Category, Company, Product


@permission_classes([AllowAny])
class RegistrationApiView(CreateAPIView):

    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)

        data = serializer.errors
        return Response(data)


@permission_classes([AllowAny])
class CategoriesView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@permission_classes([AllowAny])
class CompaniesView(ListAPIView):
    queryset = Company.objects.all().filter(is_active=True)
    serializer_class = CompanySerializer


@permission_classes([AllowAny])
class ProductView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product.objects.all(), pk=pk)
        serializer = ProductSerializer(product)
        return Response({'product': serializer.data})


@permission_classes([AllowAny])
class ActiveProductsView(ListAPIView):
    queryset = Product.objects.all().filter(is_active=True)
    serializer_class = ProductSerializer


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ModifyProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
