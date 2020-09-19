from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from booking.models import Booking
from city.models import City
from cleaner.models import Cleaner
from booking.serializer import BookingSerializer


class BookingAPI(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        city_name = request.POST.get('city_name.city_name')
        appointment_date_time = request.POST.get('appointment_date_time')
        ''' check for existing customer'''
        booking = Booking.objects.filter(phone_number=phone_number)
        city = City.objects.get(city_name=city_name)
        if booking:
            booking = booking[0]
            cleaner = Cleaner.objects.get(pk=booking.cleaner_id)
            response = {
                'message': 'You already have a booking',
                'cleanerName': f'{cleaner.first_name} {cleaner.last_name}'
            }
            return Response(response)

        ''' check for same time booking in same city'''
        bookings = Booking.objects.filter(appointment_date_time=appointment_date_time, city_name=city.pk)
        if bookings:
            cleaner_list = [book.cleaner.pk for book in bookings]
            cleaner = Cleaner.objects.filter(~Q(pk__in=cleaner_list), Q(city_name=city.pk))
        else:
            cleaner = Cleaner.objects.filter(city_name=city.pk)

        if not cleaner:
            response = {
                'message': 'Sorry non of the cleaner is not available for the combination selected time and city',
            }
            return Response(response)

        cleaner = cleaner[0]
        ''' create new booking if phone number not exist'''
        booking, created = Booking.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            city_name=city,
            cleaner=cleaner,
            appointment_date_time=appointment_date_time,
            defaults={'phone_number': phone_number},
        )

        if created:
            response = {
                'message': 'You booking is confirmed',
                'cleanerName': f'{cleaner.first_name} {cleaner.last_name}'
            }
            return Response(response)
        else:
            cleaner = Cleaner.objects.get(pk=booking.cleaner)
            response = {
                'message': 'Your already have a booking',
                'cleanerName': f'{cleaner.first_name} {cleaner.last_name}'
            }
            return Response(response)
