from rest_framework import serializers

from apps.car_license_orders.models import CarLicenseOrder
from apps.driver_license_orders.models import Governorate, LicensingUnit, OrderStatus
from apps.ratings.serializers import RatingSerializer


class GovernorateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Governorate
        fields = "__all__"


class LicensingUnitSerializer(serializers.ModelSerializer):
    governorate = GovernorateSerializer(read_only=True)

    class Meta:
        model = LicensingUnit
        fields = "__all__"


class LicensingUnitReadOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = LicensingUnit
        fields = "__all__"

class GovernorateReadOnlySerializer(serializers.ModelSerializer):
    licensing_units = LicensingUnitReadOnlySerializer(source='governorate', many=True, read_only=True)
    class Meta:
        model = Governorate
        fields = ['id', 'name', 'licensing_units']

class CarLicenseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarLicenseOrder
        fields = "__all__"
