from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Location(models.Model):
    unloc_code = models.CharField(max_length=10, unique=True)
    code = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100)
    coordinates = ArrayField(models.FloatField(), size=2)  # Array of 2 floats (latitude, longi
    province = models.CharField(max_length=100, null=True, blank=True)
    timezone = models.CharField(max_length=50, null=True, blank=True)
    alias = ArrayField(models.CharField(max_length=100), default=list, blank=True)
    regions = ArrayField(models.CharField(max_length=100), default=list, blank=True)
    unlocs = ArrayField(models.CharField(max_length=10), default=list)

    def __str__(self):
        return f"{self.name} ({self.unloc_code})"
