# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import serializers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Location
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class LocationSerializer(serializers.ModelSerializer):
    """
    A class for the location serializer
    """
    class Meta:
        model = Location
        fields = [
            'id',
            'owner',
            'name',
            'latitude',
            'longitude'
        ]

    def __str__(self):
        return self.name
