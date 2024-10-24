from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Tbl_staff(models.Model):
    S_fname = models.CharField(max_length=20)
    S_lname = models.CharField(max_length=20)
    S_email = models.EmailField(default="")
    S_gen = models.CharField(max_length=10, default="")
    S_dob = models.DateField()
    S_ph = models.CharField(max_length=10)

    S_state = models.CharField(max_length=30, default="")
    S_city = models.CharField(max_length=10)
    S_dist = models.CharField(max_length=30)
    S_pin = models.CharField(max_length=10)
    S_status = models.BooleanField()
    S_pass = models.CharField(max_length=20)
    u = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


