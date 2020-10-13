from django.db import models
from companies.models import CompanyModel


class CargoModel(models.Model):
    company = models.ForeignKey(
        CompanyModel, on_delete=models.CASCADE, related_name='applications'
    )
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
