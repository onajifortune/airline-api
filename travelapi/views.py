from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from flights.models import Flight, OnlineBooking, StationBooking

# from Flights.pagination import CustomPageNumberPagination
from travelapi.serializers import FlightSerializer, PassengerSerializer

# Create your views here.
"""
Server-side API
"""
class ListCreateFlightAPIView(ListCreateAPIView):
    serializer_class = FlightSerializer
    # pagination_class = CustomPageNumberPagination
    permission_classes = (IsAdminUser,)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, ] #DjangoFilterBackend,

    # filterset_fields = ['id', 'title', 'desc', 'is_complete', ]
    # search_fields = ['id', 'title', 'desc', 'is_complete', ]
    # ordering_fields = ['id', 'title', 'desc', 'is_complete', ]

    def get_queryset(self):
        return Flight.objects.all()

class RetrieveUpdateDestroyFlightApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = FlightSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'id'

    def get_queryset(self):
        return Flight.objects.all()


class DeleteBookingAPIView(DestroyAPIView):
    serializer_class = PassengerSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_queryset(self):
        return OnlineBooking.objects.filter(passenger=self.request.user)


"""
Client-side API
"""
class ListFlightAPIView(ListAPIView):
    serializer_class = FlightSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Flight.objects.all()


class FlightDetailAPIView(RetrieveAPIView):
    serializer_class = FlightSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Flight.objects.all()

class ListCreateBookingAPIView(ListCreateAPIView):
    serializer_class = PassengerSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        try:
            test = Flight.objects.get(pk=int(self.request.data['flights']))
            test.time.get(pk=int(self.request.data['time']))
        except:
            allowed_times = test.time.all()
            return Response({ "message": f" The selected time is not available. These are the avalable times: {list(allowed_times)}"}, status=status.HTTP_400_BAD_REQUEST, headers=headers)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    

    def perform_create(self, serializer):
        return serializer.save(passenger=self.request.user)


    def get_queryset(self):
        if self.request.user.is_staff:
            return OnlineBooking.objects.all()
        return OnlineBooking.objects.filter(passenger=self.request.user, is_active=True)


class RetrieveUpdateBookingAPIView(RetrieveUpdateAPIView):
    http_method_names = ['get', 'patch', 'head', 'options']
    serializer_class = PassengerSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        keys = list(request.data.keys())
        for i in keys:
            if i != "status":
                request.data.pop(i)
        if request.data['status'] == 'cancelled':
            request.data['is_active'] = False
        else:
            request.data['is_active'] = True
        return self.partial_update(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_staff:
            return OnlineBooking.objects.all()
        return OnlineBooking.objects.filter(passenger=self.request.user, is_active=True)

