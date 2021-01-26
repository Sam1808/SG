from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer, CategorySerializer, CompanySerializer

from .models import Category, Company


class RegistrationApiView(CreateAPIView):

    serializer_class = UserRegisterSerializer
    permission_class = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)

        data = serializer.errors
        return Response(data)


class CategoriesView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({'categories': serializer.data})


class CompaniesView(APIView):
    def get(self ,request):
        companies = Company.objects.all().filter(is_active=True)
        serializer = CompanySerializer(companies, many=True)
        return Response({'companies': serializer.data})
