from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Location
from .serializers import LocationSerializer

class LocationModelTest(TestCase):
    def test_create_location(self):
        """
        Test creating a Location instance.
        """
        location = Location.objects.create(
            unloc_code="AEAJM",
            code="52000",
            name="Ajman",
            city="Ajman",
            country="United Arab Emirates",
            alias=[],
            regions=[],
            coordinates=[55.5136433, 25.4052165],
            province="Ajman",
            timezone="Asia/Dubai",
            unlocs=["AEAJM"]
        )
        self.assertEqual(location.unloc_code, "AEAJM")
        self.assertEqual(location.name, "Ajman")


class LocationSerializerTest(TestCase):
    def test_valid_serializer(self):
        """
        Test the LocationSerializer with valid data.
        """
        data = {
            "code": "52000",
            "name": "Ajman",
            "city": "Ajman",
            "country": "United Arab Emirates",
            "alias": [],
            "regions": [],
            "coordinates": [55.5136433, 25.4052165],
            "province": "Ajman",
            "timezone": "Asia/Dubai",
            "unlocs": ["AEAJM"]
        }
        serializer = LocationSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['unlocs'][0], "AEAJM")

    def test_invalid_unloc_code(self):
        """
        Test the LocationSerializer with an invalid unloc_code.
        """
        data = {
            "code": "52000",
            "name": "Ajman",
            "city": "Ajman",
            "country": "United Arab Emirates",
            "alias": [],
            "regions": [],
            "coordinates": [55.5136433, 25.4052165],
            "province": "Ajman",
            "timezone": "Asia/Dubai",
            "unlocs": ["AE"]  # Invalid: Too short
        }
        serializer = LocationSerializer(data=data)
        self.assertFalse(serializer.is_valid())
