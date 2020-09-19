from rest_framework import viewsets
from cleaner.models import Cleaner
from cleaner.serializer import CleanerSerializer


class CleanerAPI(viewsets.ModelViewSet):
    queryset = Cleaner.objects.all()
    serializer_class = CleanerSerializer
