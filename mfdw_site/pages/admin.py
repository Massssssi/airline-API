# app/admin.py

from django.contrib import admin
from .models import Airport, Airline, Flight, Booking


class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country')


class AirlineAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'country', 'phone')


class FlightAdmin(admin.ModelAdmin):
    list_display = (
        'flight_code', 'departure_airport', 'destination_airport', 'airline', 'departure_date_time',
        'arrival_date_time',
        'duration_time', 'best_price', 'total_seats', 'available_seats')
    list_filter = ('airline', 'departure_date_time', 'arrival_date_time')
    search_fields = ('flight_code', 'departure_airport__name', 'destination_airport__name')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_ref', 'passport_number', 'flight')
    search_fields = (
        'booking_ref', 'flight__flight_code', 'flight__departure_airport__name', 'flight__destination_airport__name')


admin.site.register(Airport, AirportAdmin)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Booking, BookingAdmin)
