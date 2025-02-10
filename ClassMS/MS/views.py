from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import destination
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.models import auth
# Create your views here.

def index(request):

    return render(request, "index.html")

def about(request):

    return render(request, "about.html")

def contact(request):

    return render(request, "contact.html")



def destin(request):

    dests = destination.objects.all()

    return render(request, "destination.html", {'dests' : dests})


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Appointment has been saved')
            return render(request, 'success.html')
        
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('')    