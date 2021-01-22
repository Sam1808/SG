from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import UserRegisterSerializer


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
