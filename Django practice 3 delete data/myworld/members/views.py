from django.shortcuts import render
from .models import Users
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def show(request):
    result = Users.objects.all()

    return render(request, "index.html", {"myusers": result})


def delete(request, id):
    result = Users.objects.get(id=id)
    result.delete()

    return show(request)



