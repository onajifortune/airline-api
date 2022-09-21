from django.urls import path

from .views import (
    FlightDetailAPIView,
    ListCreateBookingAPIView,
    ListCreateFlightAPIView,
    ListFlightAPIView,
    RetrieveUpdateBookingAPIView,
    RetrieveUpdateDestroyFlightApiView,
)

urlpatterns = [
    path('', ListCreateFlightAPIView.as_view(), name="create_flight"),
    path('<int:id>', RetrieveUpdateDestroyFlightApiView.as_view(), name="modify_flight"),
    path('flights', ListFlightAPIView.as_view(), name="list_flight"),
    path('flights/<int:id>', FlightDetailAPIView.as_view(), name="detail_flights"),
    path('bookings', ListCreateBookingAPIView.as_view(), name="create_booking"),
    path('bookings/<int:id>', RetrieveUpdateBookingAPIView.as_view(), name="update_booking"),
]
