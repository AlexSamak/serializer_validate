from django.db import models
from companies.models import CompanyModel
from cargs.models import CargoModel


class ApplicationModel(models.Model):
    company = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE, related_name='app_company'
    )
    number = models.IntegerField()
    description = models.TextField()
    cargo = models.ManyToManyField('cargs.CargoModel',
                                   related_name='app_cargo')

    def __str__(self):
        return self.number
