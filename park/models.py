from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Parking(models.Model):
    CHOICES = (
        ('available', 'Available'),
        ('occupied', 'Occupied'),
    )

    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=255, default=None)
    status = models.CharField(max_length=255, choices=CHOICES, default='available')
    rate_per_hour =  models.FloatField()


class Booking(models.Model):
        CHOICES = (
            ('available', 'Available'),
            ('occupied', 'Occupied'),
        )

        user = models.ForeignKey(User, on_delete=models.CASCADE)
        parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
        hours = models.IntegerField()
        amount = models.FloatField()
