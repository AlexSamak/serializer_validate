# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import CompanyModel


# Create a model serializer
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = CompanyModel
        fields = ('name', 'description')
