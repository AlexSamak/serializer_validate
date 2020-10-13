from rest_framework import viewsets

from .serializers import CompanySerializer
from .models import CompanyModel


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CompanyModel.objects.all()

    serializer_class = CompanySerializer
