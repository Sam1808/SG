from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
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
class CategoriesView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({'categories': serializer.data})


@permission_classes([AllowAny])
class CompaniesView(APIView):
    def get(self, request):
        companies = Company.objects.all().filter(is_active=True)
        serializer = CompanySerializer(companies, many=True)
        return Response({'companies': serializer.data})


@permission_classes([AllowAny])
class ProductView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product.objects.all(), pk=pk)
        serializer = ProductSerializer(product)
        return Response({'product': serializer.data})


@permission_classes([AllowAny])
class ActiveProductsView(APIView):
    def get(self, request):
        products = Product.objects.all().filter(is_active=True)
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data})


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ModifyProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
