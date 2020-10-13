from rest_framework import viewsets

from .serializers import CargoSerializer
from .models import CargoModel


class CargoViewSet(viewsets.ModelViewSet):
    queryset = CargoModel.objects.all()

    serializer_class = CargoSerializer
