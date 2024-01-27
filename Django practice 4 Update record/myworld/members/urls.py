from django.urls import path
from . import views

urlpatterns = [
    path("", views.show, name="show"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("update/<int:id>", views.update, name="update"),
    path("update/updaterecord/<int:id>", views.updaterecord, name="updaterecord")
]





