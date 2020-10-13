from rest_framework import viewsets

from .serializers import ApplicationSerializer
from .models import ApplicationModel


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = ApplicationModel.objects.all()

    serializer_class = ApplicationSerializer
