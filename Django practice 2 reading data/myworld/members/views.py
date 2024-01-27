from django.shortcuts import render
from .models import Users


# Create your views here.


def show(request):
    result = Users.objects.all()

    return render(request, "index.html", {"myusers": result})
