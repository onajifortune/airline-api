import re

from django.conf import settings
from django.db import models

options = (
        ('approved', 'Approved'),
        ('cancelled', 'Cancelled'),
		('completed', 'Completed'),
		('incomplete', 'Incomplete')
    )

# Create your models here.

class Time(models.Model):
	time = models.TimeField(unique=True)
	date = models.DateField(auto_now=True)

	def __str__(self):
		return f'By {self.time} on {self.date}'

	def __repr__(self):
		return f'By {self.time} on {self.date}'

class Airport(models.Model):
	code = models.CharField(max_length=64)
	city = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.city} {self.code}"

class Flight(models.Model):
	origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
	destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
	duration = models.IntegerField()
	time = models.ManyToManyField(Time, blank=False, related_name='time_date')

	def __str__(self):
		return f"{self.id}: {self.origin} to {self.destination}"

	def is_valid_flight(self):
		return self.origin != self.destination and self.duration >= 0

class StationBooking(models.Model):
	first = models.CharField(max_length=64)
	last = models.CharField(max_length=64)
	flights = models.ManyToManyField(Flight, blank=True, related_name="station_passengers")

	def __str__(self):
		print(self.flights)
		return f"{self.first} {self.last}"

class OnlineBooking(models.Model):
	passenger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='current_user')
	first = models.CharField(max_length=64, blank=False)
	last = models.CharField(max_length=64, blank=False)
	flights = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="online_passengers")
	status = models.CharField(choices=options, max_length=50, default='approved', blank=False)
	is_active = models.BooleanField(blank=False, default=True)
	time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='book_time')

	def __str__(self):
		return f"{self.id}: {self.passenger}"