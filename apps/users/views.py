from django.shortcuts import render
from rest_framework import viewsets
from base.permoissions import IsAuthenticatedSuperuserOrReadOnly
from apps.users.models import User
from apps.users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedSuperuserOrReadOnly]
    serializer_class = UserSerializer