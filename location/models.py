from django.db import models
from highlights.models import Highlight


class Location(models.Model):
    highlight = models.ForeignKey(Highlight, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name
