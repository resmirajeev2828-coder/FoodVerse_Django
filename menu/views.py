from django.shortcuts import render
from django.http import JsonResponse
from .models import Menu

def menu(request):
    menus = Menu.objects.all()
    return render(request, 'menu.html', {'menus': menus})

def menu_api(request):
    menus = Menu.objects.all()

    data = []

    for item in menus:
        data.append({
            "id": item.id,
            "restaurant": item.restaurant.id,
            "name": item.name,
            "description": item.description,
            "price": str(item.price),
            "image": item.image.url if item.image else ""
        })

    return JsonResponse(data, safe=False)