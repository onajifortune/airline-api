# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from flights.models import Flight
from users.models import User

# Create your tests here.

class FlightsAPITestCase(APITestCase):

    def create_flight(self):
        sample_flight = {'origin': 1, 'destination': 2, 'duration': 1, 'time': 1}
        response = self.client.post(reverse('create_flight'), sample_flight)

        return response

    def authenticate(self):
        self.client.post(reverse("register"), {
            "username": "username",
            "email": "a@a.com",
            "password": "password"
        })

        response = self.client.post(reverse('login'), {
            'email': 'a@a.com',
            'password': 'password',
        })
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")
    

class TestListCreateFlights(FlightsAPITestCase):
    def tests_should_not_create_Flight_if_not_authorized(self):
        response = self.create_flight()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def tests_should_not_create_flight_if_not_staff(self):
        response = self.create_flight()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def tests_should_create_flight_if_is_staff(self):
        previous_Flight_count = Flight.objects.all().count()
        self.authenticate()
        response = self.create_flight()
        self.assertEqual(Flight.objects.all().count(), previous_Flight_count + 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        {'origin': 1, 'destination': 2, 'duration': 1, 'time': 1}
        self.assertEqual(response.data['origin'], 1)
        self.assertEqual(response.data['destination'], 2)
        self.assertEqual(response.data['duration'], 1)
        self.assertEqual(response.data['time'], 1)

