from django.db import models


class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    booking_date = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.customer_name} - {self.event_type} ({self.booking_date})"
