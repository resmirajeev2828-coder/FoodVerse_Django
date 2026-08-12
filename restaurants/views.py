from django.shortcuts import render, get_object_or_404
from .models import Restaurant
from django.db.models import Q
from django.http import JsonResponse

def restaurants(request):
    search = request.GET.get("search")

    if search:
        restaurants = Restaurant.objects.filter(
            Q(name__icontains=search)
        )
    else:
        restaurants = Restaurant.objects.all()

    return render(request, "restaurants.html", {"restaurants": restaurants})


def restaurant_detail(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    return render(request, "restaurant_detail.html", {"restaurant": restaurant})

def restaurant_api(request):
    restaurants = Restaurant.objects.all()

    data = []

    for restaurant in restaurants:
        data.append({
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
            "rating": restaurant.rating,
            "image": restaurant.image.url if restaurant.image else ""
        })

    return JsonResponse(data, safe=False)

def restaurant_detail_api(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)

    data = {
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "rating": restaurant.rating,
        "image": restaurant.image.url if restaurant.image else ""
    }

    return JsonResponse(data)