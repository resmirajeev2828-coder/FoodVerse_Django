from django.shortcuts import render
from .models import Offer

def offers(request):
    offers = Offer.objects.all()
    return render(request, "offers.html", {"offers": offers})