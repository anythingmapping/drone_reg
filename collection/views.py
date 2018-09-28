from django.shortcuts import render
from django.http import HttpResponse
from collection.models import Drone

def index(request):
    drones = Drone.objects.all()
    
    return render(request, 'index.html', {'drones':drones})
