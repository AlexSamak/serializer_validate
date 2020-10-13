from rest_framework import serializers
from .models import ApplicationModel


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationModel
        fields = '__all__'

    def validate_cargo(self, value):
        for item in value:
            print(item.id)
            if item.id != 1:
                raise serializers.ValidationError("Company bad !!!")
        return value
