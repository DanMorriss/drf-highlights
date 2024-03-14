from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)

    def __str__(self):
        return self.name
