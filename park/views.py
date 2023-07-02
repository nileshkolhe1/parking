from django.shortcuts import render, redirect
from park.models import Parking, Booking
from geopy import distance

# Create your views here.

def index(request):
    parkings = Parking.objects.filter(status='available')
    return render(request, 'index.html', context={'parkings': parkings})


def search(request):
    available_parkings = []
    if request.method == 'POST':
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        radius = request.POST['radius']
        user_location = (latitude, longitude)
        parkings = Parking.objects.all()
        for parking in parkings:
            parking_location = (parking.latitude, parking.longitude)
            parking_distance = distance.distance(user_location, parking_location).m
            if parking_distance <= int(radius) and parking.status == 'available':
                available_parkings.append(
                    {
                        'id': parking.id,
                        'address': parking.address,
                        'latitude': parking.latitude,
                        'longitude': parking.longitude,
                        'status': parking.status,
                        'rate_per_hour': parking.rate_per_hour,
                        'distance': parking_distance,
                    }
                )

    return render(request, 'search.html', context={'available_parkings': available_parkings})


def book(request):
    if request.method == 'POST':
        hours = request.POST['hours']
        amount = request.POST['amount']
        parking_id = request.POST['parking_id']

        parking = Parking.objects.get(pk=parking_id)
        parking.status = "occupied"
        parking.save()

        booking = Booking.objects.create(
            hours=hours,
            amount=amount,
            parking=parking,
            user=request.user
        )
    return redirect('/park/search')


def myParkings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my-bookings.html', context={'bookings': bookings})
