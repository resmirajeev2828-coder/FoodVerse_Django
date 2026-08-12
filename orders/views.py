from django.shortcuts import render, redirect
from .models import Cart, Order
from menu.models import Menu
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required

from .models import Order
from menu.models import Menu


@login_required
def add_to_cart(request, id):
    menu = Menu.objects.get(id=id)

    cart_item, created = Cart.objects.get_or_create(
        menu=menu,
        defaults={"quantity": 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")

@login_required
def cart(request):
    cart_items = Cart.objects.all()
    total = 0

    for item in cart_items:
        total += item.menu.price * item.quantity

    return render(request, "cart.html", {
        "cart_items": cart_items,
        "total": total
    })

@login_required
def checkout(request):
    cart_items = Cart.objects.all()

    for item in cart_items:
        Order.objects.create(
            user=request.user,
            menu=item.menu,
            quantity=item.quantity
        )

    cart_items.delete()

    return redirect("order_success")

@login_required
def order_success(request):
    return render(request, "order_success.html")

from .models import Order
from django.contrib.auth.decorators import login_required

@login_required
def order_history_api(request):
    orders = Order.objects.filter(user=request.user).order_by("-id")

    data = []

    for order in orders:
        data.append({
            "id": order.id,
            "menu": order.menu.name,
            "quantity": order.quantity,
            "price": float(order.menu.price),
            "total": float(order.menu.price * order.quantity),
        })

    return JsonResponse(data, safe=False)

@login_required
def remove_from_cart(request, id):
    item = get_object_or_404(Cart, id=id)
    item.delete()
    return redirect("cart")

def get_cart(request):
    cart_items = Cart.objects.all()

    items = []

    for item in cart_items:
        items.append({
            "id": item.menu.id,
            "quantity": item.quantity,
        })

    return JsonResponse({
        "items": items
    })

@login_required
def increase_quantity(request, id):
    cart_item = get_object_or_404(Cart, id=id)

    cart_item.quantity += 1
    cart_item.save()

    return redirect("cart")


@login_required
def decrease_quantity(request, id):
    cart_item = get_object_or_404(Cart, id=id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect("cart")


@login_required
def remove_from_cart(request, id):
    cart_item = get_object_or_404(Cart, id=id)
    cart_item.delete()

    return redirect("cart")


@csrf_exempt
@login_required
def create_order(request):
    if request.method == "POST":
        data = json.loads(request.body)

        items = data.get("items", [])

        orders = []

        for item in items:
            menu = Menu.objects.get(id=item["id"])

            quantity = item.get("quantity", 1)
            total = menu.price * quantity

            order = Order.objects.create(
                user=request.user,
                menu=menu,
                quantity=quantity,
                total=total
            )

            orders.append(order.id)

        return JsonResponse({
            "message": "Order placed successfully",
            "order_ids": orders
        })

    return JsonResponse(
        {"error": "POST method required"},
        status=400
    )