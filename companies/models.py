from django.db import models
from django.contrib.auth.models import User


class CompanyModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name="profile")
    _current_company = models.ForeignKey(
        'companies.CompanyModel',
        on_delete=models.PROTECT,
        related_name="profiles",
        null=True
    )

    @property
    def current_company(self):
        if self._current_company:
            return self._current_company
