from django.db import IntegrityError
import re
from rest_framework import serializers

from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for Locations model
    """

    class Meta:
        model = Location
        fields = [
            'unloc_code',
            'code',
            'name',
            'city',
            'country',
            'alias',
            'regions',
            'coordinates',
            'province',
            'timezone',
            'unlocs'
        ]
        read_only_fields = ["unloc_code"]

    def validate_unloc_code(self, value):
        """
        Validate that the unloc_code is exactly 5 characters long and contains only uppercase letters and numbers.
        """
        if not re.match(r'^[A-Z0-9]{5}$', value):
            raise serializers.ValidationError("unloc must be exactly 5 characters long and contain only uppercase letters and numbers.")
        return value

    def validate(self, data):
        """
        Validate the input data and compute unloc_code from the unlocs list.
        """
        unlocs = data.get('unlocs', [])

        # Ensure unlocs is a list and has at least one item
        if not isinstance(unlocs, list) or len(unlocs) == 0:
            raise serializers.ValidationError("The 'unlocs' field must be a non empty list.")

        # Validate each unloc code
        for unloc in unlocs:
            self.validate_unloc_code(unloc)

        # Compute unloc_code from the first item in the unlocs list
        data['unloc_code'] = unlocs[0]
        return data

    def create(self, validated_data):
        """
        Create a new Location instance and handle IntegrityError.
        """
        try:
            return Location.objects.create(**validated_data)
        except IntegrityError as e:
            raise serializers.ValidationError({"unloc_code": "A location with this unloc_code already exists."})

    def update(self, instance, validated_data):
        """
        Update an existing Location instance and handle IntegrityError.
        """

        # Recompute unloc_code if unlocs is updated
        new_unloc_code = validated_data['unloc_code']
        if new_unloc_code != instance.unloc_code:
            # Check if the new unloc_code already exists
            if Location.objects.filter(unloc_code=new_unloc_code).exists():
                raise serializers.ValidationError({"unloc_code": "A location with this unloc_code already exists."})
            instance.unloc_code = new_unloc_code

        # Update other fields
        instance.code = validated_data.get('code', instance.code)
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.alias = validated_data.get('alias', instance.alias)
        instance.regions = validated_data.get('regions', instance.regions)
        instance.coordinates = validated_data.get('coordinates', instance.coordinates)
        instance.province = validated_data.get('province', instance.province)
        instance.timezone = validated_data.get('timezone', instance.timezone)
        instance.unlocs = validated_data.get('unlocs', instance.unlocs)
        try:
            instance.save()
            return instance
        except IntegrityError as e:
            raise serializers.ValidationError({"unloc_code": "A location with this unloc_code already exists."})
