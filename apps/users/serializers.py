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
        fields = ['name','phone','id','email','username','password']

        read_only_fields = ['id']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
            instance.save()
        return instance



# class CustomRegisterSerializer(RegisterSerializer):
#     username = None


class CustomLoginSerializer(LoginSerializer):
    username = None
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={'input_type': 'password'})


class CustomUserDetailsSerializer(UserDetailsSerializer):

    class Meta(UserDetailsSerializer.Meta):
        fields = ['id', 'email', 'phone', 'name',]


class CustomRegisterSerializer(RegisterSerializer):
    phone = serializers.CharField(max_length=15, required=True)

    def custom_signup(self, request, user):
        print('calllled')
        user.phone = self.validated_data.get('phone')
        user.save()