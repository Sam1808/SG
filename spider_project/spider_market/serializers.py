from rest_framework.serializers import ModelSerializer
from .models import User


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def save(self, *args, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        user.set_password(password)

        user.save()
        return user