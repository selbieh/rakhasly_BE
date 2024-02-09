from rest_framework import serializers


from apps.driver_license_orders.models import DriverLicenseOrder, Governorate, LicensingUnit
from apps.ratings.serializers import RatingSerializer
from apps.users.serializers import UserSerializer


class GovernorateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Governorate
        fields = "__all__"


class LicensingUnitReadOnlySerializer(serializers.ModelSerializer):
    governorate = GovernorateSerializer(read_only=True)

    class Meta:
        model = LicensingUnit
        fields = "__all__"


class LicensingUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = LicensingUnit
        fields = "__all__"

class GovernorateReadOnlySerializer(serializers.ModelSerializer):
    licensing_units = LicensingUnitSerializer(source='governorate', many=True, read_only=True)
    class Meta:
        model = Governorate
        fields = ['id', 'name', 'licensing_units']

class DriverLicenseOrderSerializer(serializers.ModelSerializer):
    licensing_units = LicensingUnitSerializer(read_only=True)

    class Meta:
        model = DriverLicenseOrder
        fields = "__all__"


class DriverLicenseReadOnlyOrderSerializer(serializers.ModelSerializer):
    licensing_unit = LicensingUnitSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    rating = RatingSerializer(read_only=True)


    class Meta:
        model = DriverLicenseOrder
        fields = "__all__"
