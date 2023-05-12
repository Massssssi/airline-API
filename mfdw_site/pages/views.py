import json

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from .models import Airport, Flight, Booking, Airline


@csrf_exempt
@require_POST
def create_booking(request):
    # retrieve booking data from request.POST
    booking_ref = request.POST.get('booking_ref')
    passport_number = request.POST.get('passport_number')
    flight_id = request.POST.get('flight_id')

    # create a new booking object in the database
    try:
        flight = Flight.objects.get(id=flight_id)
        booking = Booking.objects.create(booking_ref=booking_ref, passport_number=passport_number, flight=flight)
        response_data = {'success': True, 'booking_id': booking.id}
    except Flight.DoesNotExist:
        response_data = {'success': False, 'error': 'Invalid flight ID'}

    # return a JSON response with the result of the operation
    return JsonResponse(response_data)


@csrf_exempt
@require_POST
def delete_booking(request):
    # retrieve booking ID from request.POST
    booking_id = request.POST.get('booking_id')

    # delete the booking object from the database
    try:
        booking = Booking.objects.get(id=booking_id)
        booking.delete()
        response_data = {'success': True}
    except Booking.DoesNotExist:
        response_data = {'success': False, 'error': 'Invalid booking ID'}

    # return a JSON response with the result of the operation
    return JsonResponse(response_data)


@csrf_exempt
def add_flight(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        departure_airport_id = data['departure_airport_id']
        destination_airport_id = data['destination_airport_id']
        airline_id = data['airline_id']
        flight_code = data['flight_code']
        departure_date_time = data['departure_date_time']
        arrival_date_time = data['arrival_date_time']
        duration_time = data['duration_time']
        best_price = data['best_price']
        total_seats = data['total_seats']
        available_seats = data['available_seats']

        departure_airport = Airport.objects.get(id=departure_airport_id)
        destination_airport = Airport.objects.get(id=destination_airport_id)
        airline = Airline.objects.get(id=airline_id)

        flight = Flight(departure_airport=departure_airport,
                        destination_airport=destination_airport,
                        airline=airline,
                        flight_code=flight_code,
                        departure_date_time=departure_date_time,
                        arrival_date_time=arrival_date_time,
                        duration_time=duration_time,
                        best_price=best_price,
                        total_seats=total_seats,
                        available_seats=available_seats)
        flight.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Invalid request method'})


@csrf_exempt
def delete_flight(request, flight_id):
    if request.method == 'DELETE':
        try:
            flight = Flight.objects.get(id=flight_id)
            flight.delete()
            return JsonResponse({'success': True})
        except Flight.DoesNotExist:
            return JsonResponse({'error': 'Flight does not exist'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
