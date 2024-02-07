from django.shortcuts import render
from rest_framework import viewsets
from base.permoissions import IsAuthenticatedSuperuserOrReadOnly
from apps.users.models import User
from apps.users.serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedSuperuserOrReadOnly]
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields= ['name', 'email', 'is_active', 'is_staff']