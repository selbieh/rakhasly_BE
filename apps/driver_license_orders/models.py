from django.db import models
from rest_framework.serializers import ValidationError

from apps.ratings.models import Rating
from apps.users.models import User
from config.models import AbstractBaseModel


class Governorate(AbstractBaseModel):
    name = models.CharField(max_length=64)


class LicensingUnit(AbstractBaseModel):
    name = models.CharField(max_length=64)
    governorate = models.ForeignKey(Governorate, on_delete=models.CASCADE, related_name='governorate')


class DriverLicenseOrder(AbstractBaseModel):

    RENEWAL_DURATION_CHOICES = [
        (1, '1 Year'),
        (2, '2 Years'),
        (3, '3 Years'),
    ]

    needs_check = models.BooleanField(default=False)
    governorate = models.ForeignKey(Governorate, on_delete=models.PROTECT)
    licensing_unit = models.ForeignKey(LicensingUnit, on_delete=models.PROTECT)
    renewal_duration = models.IntegerField(choices=RENEWAL_DURATION_CHOICES)
    visit_date = models.DateTimeField()
    visit_slot = models.CharField(max_length=32, null=True, blank=True)
    vip_assistance = models.BooleanField(default=False)
    is_new_car = models.BooleanField(default=False)
    contract_image = models.ImageField(upload_to='contracts/', null=True, blank=True)
    license_id_image = models.ImageField(upload_to='license_ids/', null=True, blank=True)
    national_id_image = models.ImageField(upload_to='national_ids/')
    user = models.ForeignKey(User, related_name='driver_license_user', null=True, on_delete=models.PROTECT)
    rating = models.OneToOneField(Rating, related_name='driver_license_rating', null=True, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if not self.pk and self.is_new_car and not self.contract_image:
            raise ValidationError({"contract": "contract image is required"})

        super().save(*args, **kwargs)
