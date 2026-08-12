from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def offers(request):
    return render(request, 'offers.html')
