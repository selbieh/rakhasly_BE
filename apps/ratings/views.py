from rest_framework import viewsets

from apps.ratings.models import Rating
from apps.ratings.serializers import RatingSerializer
from rest_framework.permissions import IsAuthenticated


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]