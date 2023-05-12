from django.urls import path
from . import views

urlpatterns = [
    path('create/bookings', views.create_booking, name='create_booking'),
    path('delete/bookings', views.delete_booking, name='delete_booking'),
    path('add/flight', views.add_flight, name='add_flight'),
    path('delete/flight', views.add_flight, name='delete_flight'),
]
