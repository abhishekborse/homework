from django.db import models
from city.models import City
from cleaner.models import Cleaner
from django.core.validators import RegexValidator


alpha_only = RegexValidator(r'^[a-zA-Z ]*$', 'Only Characters are allowed.')
phone_number_only = RegexValidator(r'^[0-9]{10}*$', 'Only 10 Numbers are allowed.')


# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=100, validators=[alpha_only])
    last_name = models.CharField(max_length=100, validators=[alpha_only])
    phone_number = models.CharField(max_length=15, validators=[phone_number_only])
    city_name = models.ForeignKey(City, on_delete=models.CASCADE)
    cleaner = models.ForeignKey(Cleaner, on_delete=models.CASCADE)
    appointment_date_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        pass
        # ordering = ['appointment_date_time']
