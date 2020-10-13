from rest_framework import serializers
from .models import ApplicationModel
from serializer_validate.validators import CompanyForeignKeyValidator


def multiple_of_ten(value):
    print(value)
    if value != 1:
        raise serializers.ValidationError("Number the bad !!!")
    return value


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationModel
        fields = '__all__'

        extra_kwargs = {
            'number': {'validators': [CompanyForeignKeyValidator(lambda company: company.agents)]}
        }


    # def validate_cargo(self, value):
    #     for item in value:
    #         print(item.id)
    #         if item.id != 1:
    #             raise serializers.ValidationError("Company bad !!!")
    #     return value
