from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.driver_license_orders.views import GovernorateViewSet, LicensingUnitViewSet

from apps.car_license_orders.views import CarLicenseOrderViewSet

router = DefaultRouter()
router.register(r'car-license', CarLicenseOrderViewSet, basename='car-license')


urlpatterns = [
    path('', include(router.urls)),
]
