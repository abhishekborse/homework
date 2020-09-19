from django.db import models
from city.models import City


# Create your models here.
class Cleaner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city_name = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        pass
        # ordering = ['appointment_date_time']
