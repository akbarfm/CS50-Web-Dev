from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Flight, Airport, Passenger
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'flights/index.html', {
        'flights': Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flight=flight).all()
    return render(request, 'flights/flight.html', {
        "flight": flight,
        'passengers': passengers,
        'non_passengers': non_passengers,
    })

def book(request, flight_id):
    if request.method == 'POST':

        flight = Flight.objects.get(pk=flight_id)

        passenger_id = int(request.POST['passenger'])

        passenger = Passenger.objects.get(pk=passenger_id)

        passenger.flight.add(flight)

        return HttpResponseRedirect(reverse('flight', args=[flight.id,]))

def cancel(request, flight_id):
    if request.method == 'POST':
        flight = Flight.objects.get(pk=flight_id)
        passenger_id = int(request.POST['passenger'])
        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flight.remove(flight)
        return HttpResponseRedirect(reverse('flight', args=(flight.id,)))