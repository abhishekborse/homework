from rest_framework import viewsets
from rest_framework import permissions
from city.models import City
from city.serializer import CitySerializer


class CityAPI(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    # permission_classes = [permissions.IsAuthenticated]

