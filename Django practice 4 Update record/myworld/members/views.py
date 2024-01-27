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


def update(request, id):
    myuser = Users.objects.get(id=id)

    return render(request, "update.html", {"myuser":myuser})

def updaterecord(request, id):
    username1 = request.POST['username1']
    password1 = request.POST['password1']

    myuser = Users.objects.get(id=id)

    myuser.username1 = username1
    myuser.password1 = password1

    myuser.save()

    return show(request)



