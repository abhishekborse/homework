from rest_framework import serializers
from .models import Cleaner


class CleanerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaner
        fields = '__all__'
