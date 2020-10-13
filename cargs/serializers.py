from rest_framework import serializers
from .models import CargoModel


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoModel
        fields = '__all__'
