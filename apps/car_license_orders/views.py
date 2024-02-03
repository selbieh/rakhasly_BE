from rest_framework import viewsets
from rest_framework import status, throttling
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.permissions import DjangoModelPermissions

from apps.car_license_orders.models import CarLicenseOrder
from apps.car_license_orders.serializers import  CarLicenseOrderSerializer


class CarLicenseOrderViewSet(viewsets.ModelViewSet):
    queryset = CarLicenseOrder.objects.all()
    permission_classes = [DjangoModelPermissions]
    serializer_class = CarLicenseOrderSerializer

    def create(self, request, *args, **kwargs):
        # set order user to authenticated user
        request.data['user'] = request.user.id

        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response(str(e.detail), status=status.HTTP_400_BAD_REQUEST)