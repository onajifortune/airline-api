from django.conf import settings
from rest_framework import serializers

from flights.models import Flight, OnlineBooking


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('id', 'origin', 'destination', 'duration', 'time')

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineBooking
        fields = ('id', 'passenger', 'first', 'last', 'flights', 'time', 'status', 'is_active')

        # read_only_fields = ('is_active',)