# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import generics
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Location
from .serializers import LocationSerializer
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class LocationList(generics.ListCreateAPIView):
    """
    A class for the location list
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class for the location detail
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
