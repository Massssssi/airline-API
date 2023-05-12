from django.db import models


class Airport(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.city}, {self.country})"


class Airline(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Flight(models.Model):
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    flight_code = models.CharField(max_length=10)
    departure_date_time = models.DateTimeField()
    arrival_date_time = models.DateTimeField()
    duration_time = models.DurationField()
    best_price = models.DecimalField(max_digits=8, decimal_places=2)
    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.flight_code}: {self.departure_airport} -> {self.destination_airport}"


class Booking(models.Model):
    booking_ref = models.CharField(max_length=10)
    passport_number = models.CharField(max_length=20)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return self.booking_ref
