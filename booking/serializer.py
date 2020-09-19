from rest_framework import serializers

from city.serializer import CitySerializer
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    city_name = CitySerializer(many=False)

    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'phone_number', 'city_name', 'appointment_date_time']
