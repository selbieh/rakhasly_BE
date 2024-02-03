from rest_framework import viewsets
from rest_framework import status, throttling
from apps.driver_license_orders.models import Governorate, LicensingUnit
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.permissions import DjangoModelPermissions

from apps.driver_license_orders.serializers import GovernorateSerializer, LicensingUnitSerializer, \
    GovernorateReadOnlySerializer

from apps.driver_license_orders.models import DriverLicenseOrder
from apps.driver_license_orders.serializers import DriverLicenseOrderSerializer


class LicensingUnitViewSet(viewsets.ModelViewSet):
    queryset = LicensingUnit.objects.all()
    serializer_class = LicensingUnitSerializer
    # permission_classes = []

class GovernorateViewSet(viewsets.ModelViewSet):
    queryset = Governorate.objects.all()
    serializer_class = GovernorateSerializer
    # permission_classes = []

    def get_serializer_class(self):
        if self.action == 'list':
            return GovernorateReadOnlySerializer

        return GovernorateSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

class DriverLicenseOrderViewSet(viewsets.ModelViewSet):
    queryset = DriverLicenseOrder.objects.all()
    permission_classes = [DjangoModelPermissions]
    serializer_class = DriverLicenseOrderSerializer

    def create(self, request, *args, **kwargs):
        # set order user to authenticated user
        request.data['user'] = request.user.id

        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response(str(e.detail), status=status.HTTP_400_BAD_REQUEST)