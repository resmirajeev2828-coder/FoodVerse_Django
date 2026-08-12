from django.shortcuts import render
from .models import Contact

def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            subject=request.POST["subject"],
            message=request.POST["message"]
        )
        return render(request, "contact.html", {"success": True})

    return render(request, "contact.html", {"success": True})