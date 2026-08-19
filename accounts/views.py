from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

@login_required
def profile(request):
    return render(request, "profile.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        print(user)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "register.html")

@csrf_exempt
def register_api(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "success": False,
                "message": "Username already exists!"
            }, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({
                "success": False,
                "message": "Email already exists!"
            }, status=400)

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return JsonResponse({
            "success": True,
            "message": "Registration successful!"
        })

    return JsonResponse({
        "success": False,
        "message": "POST request required"
    }, status=405)
        


def logout_view(request):
    logout(request)
    return redirect("login")

@csrf_exempt
def login_api(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)

            return JsonResponse({
                "success": True,
                "message": "Login successful!",
                "username": user.username
            })

        return JsonResponse({
            "success": False,
            "message": "Invalid username or password!"
        }, status=400)

    return JsonResponse({
        "success": False,
        "message": "POST request required"
    }, status=405) 

 