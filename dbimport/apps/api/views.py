# Create your views here.
from rest_framework import generics
from .models import Location
from .serializers import LocationSerializer


class LocationListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating locations.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a location.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = 'unloc_code'  # Use unloc_code as the lookup field
