from django.urls import path, include
from .views import LocationListCreateView, LocationRetrieveUpdateDestroyView

app_name = 'api'

urlpatterns = [
    path('locations/', LocationListCreateView.as_view(), name='location-list-create'),
    path('locations/<str:unloc_code>/', LocationRetrieveUpdateDestroyView.as_view(), name='location-retrieve-update-destroy'),
]
