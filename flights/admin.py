from django.contrib import admin

from .models import Airport, Flight, OnlineBooking, StationBooking, Time


# Register your models here.
class FlightAdmin(admin.ModelAdmin):
	list_display = ("id", "origin", "destination", "duration")
	filter_horizontal = ('time',)
	"""docstring fos FlightAdmin"""
		
class StationPassengerAdmin(admin.ModelAdmin):
	filter_horizontal = ("flights", )
	"""docstring for PassengerAdmin"""

class TimeAdmin(admin.ModelAdmin):
	list_display = ("id", "time", "date")
	"""docstring fos TimeAdmin"""

class OnlineBookingAdmin(admin.ModelAdmin):
	list_display = ("id", "first", "last", "flights")
	"""docstring for PassengerAdmin"""
		

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(StationBooking, StationPassengerAdmin)
admin.site.register(OnlineBooking, OnlineBookingAdmin)
admin.site.register(Time, TimeAdmin,)
