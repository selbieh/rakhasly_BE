from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.driver_license_orders.views import GovernorateViewSet, LicensingUnitViewSet

from apps.driver_license_orders.views import DriverLicenseOrderViewSet

router = DefaultRouter()
router.register(r'governorates', GovernorateViewSet, basename='governorate')
router.register(r'licensing-units', LicensingUnitViewSet, basename='licensin-_unit')
router.register(r'driver-license', DriverLicenseOrderViewSet, basename='driver-license')


urlpatterns = [
    path('', include(router.urls)),
]
