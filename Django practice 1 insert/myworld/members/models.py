from django.db import models




# Create your models here.

class Users(models.Model):
    username1 = models.CharField(max_length=90)
    password1 = models.CharField(max_length=90)

    class Meta:
        try:
            db_table = "users"
        except Exception as e:
            print("sorry something went wrong", e)

