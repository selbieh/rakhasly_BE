from rest_framework import serializers

from apps.car_license_orders.models import CarLicenseOrder
from apps.driver_license_orders.models import Governorate, LicensingUnit, OrderStatus
from apps.driver_license_orders.serializers import LicensingUnitSerializer
from apps.ratings.serializers import RatingSerializer
from apps.users.serializers import UserSerializer

class CarLicenseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarLicenseOrder
        fields = "__all__"


class CarLicenseReadOnlyOrderSerializer(serializers.ModelSerializer):
    licensing_unit = LicensingUnitSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = CarLicenseOrder
        fields = "__all__"
