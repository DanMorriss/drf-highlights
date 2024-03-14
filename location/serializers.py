from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
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
