from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.driver_license_orders.views import GovernorateViewSet, LicensingUnitViewSet

from apps.car_license_orders.views import CarLicenseOrderViewSet

router = DefaultRouter()
router.register(r'governorates', GovernorateViewSet, basename='governorate')
router.register(r'licensing_units', LicensingUnitViewSet, basename='licensing_unit')
router.register(r'car_license', CarLicenseOrderViewSet, basename='car_license')


urlpatterns = [
    path('', include(router.urls)),
]
