from rest_framework import viewsets
from rest_framework import status, throttling
from apps.driver_license_orders.models import Governorate, LicensingUnit
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.permissions import DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from datetime import datetime
from django.utils import timezone

from rest_framework.permissions import IsAuthenticated

# from drf_standardized_errors import exceptions

from apps.driver_license_orders.serializers import GovernorateSerializer, LicensingUnitSerializer, \
    GovernorateReadOnlySerializer, DriverLicenseReadOnlyOrderSerializer

from apps.driver_license_orders.models import DriverLicenseOrder
from apps.driver_license_orders.serializers import DriverLicenseOrderSerializer
from base.permoissions import IsAuthenticatedSuperuserOrReadOnly


class LicensingUnitViewSet(viewsets.ModelViewSet):
    queryset = LicensingUnit.objects.all()
    serializer_class = LicensingUnitSerializer
    permission_classes = [IsAuthenticatedSuperuserOrReadOnly]

class GovernorateViewSet(viewsets.ModelViewSet):
    queryset = Governorate.objects.all()
    serializer_class = GovernorateSerializer
    permission_classes = [IsAuthenticatedSuperuserOrReadOnly]

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
    permission_classes = [IsAuthenticated]
    # serializer_class = DriverLicenseOrderSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields= ['status', 'vip_assistance', 'installment', 'is_new_car', 'needs_check']
    search_fields = ['user__name']

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return DriverLicenseOrderSerializer
        else:
            return DriverLicenseReadOnlyOrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        from_date_str = self.request.query_params.get('from_date')
        to_date_str = self.request.query_params.get('to_date')

        if from_date_str:
            from_date = datetime.utcfromtimestamp(int(from_date_str) / 1000).date()
            queryset = queryset.filter(created_at__date__gte=from_date)

        if to_date_str:
            to_date = datetime.utcfromtimestamp(int(to_date_str) / 1000).date()
            to_date += timezone.timedelta(days=1)
            queryset = queryset.filter(created_at__date__lt=to_date)

        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)
        return queryset


    def create(self, request, *args, **kwargs):
        # set order user to authenticated user
        request.data['user'] = request.user.id

        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            # raise exceptions.BadRequestError(detail=str(e.detail),status=status.HTTP_400_BAD_REQUEST)
            return Response(str(e.detail), status=status.HTTP_400_BAD_REQUEST)

