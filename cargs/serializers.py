# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import CargoModel


# Create a model serializer
class CargoSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = CargoModel
        fields = ('company', 'name', 'description')
