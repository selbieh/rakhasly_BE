from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from apps.users.models import User
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from rest_framework.views import APIView
from dj_rest_auth.serializers import UserDetailsSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }


# class CustomRegisterSerializer(RegisterSerializer):
#     username = None


class CustomLoginSerializer(LoginSerializer):
    username = None
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={'input_type': 'password'})


class CustomUserDetailsSerializer(UserDetailsSerializer):

    class Meta(UserDetailsSerializer.Meta):
        fields = ['id', 'email', 'phone', 'name',]

