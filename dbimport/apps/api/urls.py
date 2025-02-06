from django.urls import path, include
from .views import LocationListCreateView, LocationRetrieveUpdateDestroyView

app_name = 'api'

router = DefaultRouter()
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('locations/', LocationListCreateView.as_view(), name='location-list-create'),
    path('locations/<str:unloc_code>/', LocationRetrieveUpdateDestroyView.as_view(), name='location-retrieve-update-destroy'),
]