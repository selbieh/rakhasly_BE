# ratings/models.py

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from config.models import AbstractBaseModel


class Rating(AbstractBaseModel):

    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5.0)])
    comment = models.CharField(max_length=256)
