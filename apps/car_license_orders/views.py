from rest_framework import viewsets
from rest_framework import status, throttling
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.permissions import DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from datetime import datetime
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated


from apps.car_license_orders.models import CarLicenseOrder
from apps.car_license_orders.serializers import CarLicenseOrderSerializer, CarLicenseReadOnlyOrderSerializer


class CarLicenseOrderViewSet(viewsets.ModelViewSet):
    queryset = CarLicenseOrder.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CarLicenseOrderSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields= ['status', 'vip_assistance', 'installment', 'is_new_car', 'needs_check']
    search_fields = ['user__name']

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CarLicenseOrderSerializer
        else:
            return CarLicenseReadOnlyOrderSerializer

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
            return Response(str(e.detail), status=status.HTTP_400_BAD_REQUEST)