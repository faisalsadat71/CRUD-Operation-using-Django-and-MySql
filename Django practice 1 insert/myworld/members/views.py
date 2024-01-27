from django.shortcuts import render
from members.models import Users
from django.contrib import messages
# Create your views here.


def insertrecord(request):
    if request.method == "POST":
        if request.POST.get("username1") and request.POST.get("password1"):
            saverecord = Users()
            saverecord.username1 = request.POST.get("username1")
            saverecord.password1 = request.POST.get("password1")
            saverecord.save()
            messages.success(request, "Record successfully added...")

            return render(request, "index.html")
    else:
            return render(request, "index.html")


