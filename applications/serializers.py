# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import ApplicationModel


# Create a model serializer
class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = ApplicationModel
        fields = ('number', 'description')