from rest_framework import viewsets

from data.api.serializers import HeroSerializer
from data.models import Hero


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by("name")
    serializer_class = HeroSerializer
