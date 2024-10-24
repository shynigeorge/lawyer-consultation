from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from advocate.models import Tbl_adv


class DemoUser(AbstractUser):
    is_advocate = models.BooleanField(default=False)


# Create your models here.
class Tbl_cust(models.Model):
    C_fname = models.CharField(max_length=20)
    C_lname = models.CharField(max_length=20)
    C_email = models.EmailField(default="")
    C_gen = models.CharField(max_length=10, default="")
    C_dob = models.DateField()
    C_ph = models.CharField(max_length=10)
    C_state = models.CharField(max_length=30, default="")
    C_city = models.CharField(max_length=10)
    C_dist = models.CharField(max_length=30)
    C_pin = models.CharField(max_length=10)
    C_status = models.BooleanField()
    C_pass = models.CharField(max_length=20)
    u = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.C_fname




option=(
    ('pending','pending'),
    ('approved','approved'),
    ('rejected','rejected'),

)

class booking(models.Model):
    customer=models.ForeignKey(Tbl_cust,on_delete=models.CASCADE,default="")
    adv = models.ForeignKey(Tbl_adv, on_delete=models.CASCADE)
    payment = models.PositiveIntegerField(null=True)
    status=models.CharField(max_length=30,choices=option,default='pending')
    date=models.DateField(auto_now_add=True,null=True)
    paid = models.CharField(max_length=20,choices=(('paid','paid'),('rejected','rejected'),('not-paid','not-paid')),default='not-paid')

    def __str__(self):
        return self.customer.C_fname


class case(models.Model):
    booking=models.ForeignKey(booking,on_delete=models.CASCADE,default=1)
    customer = models.ForeignKey(Tbl_cust, on_delete=models.CASCADE,default='')
    adv = models.ForeignKey(Tbl_adv, on_delete=models.CASCADE)
    case_details = models.CharField(max_length=30)
    document = models.FileField(upload_to='case_details',null=True)

    def __str__(self):
        return self.adv.Adv_fname

class Customer_card_details_class(models.Model):
    customer = models.ForeignKey(Tbl_cust,on_delete=models.CASCADE)
    card_no = models.CharField(max_length=16)
    card_holder_name=models.CharField(max_length=20,null=True)
    expiry_date = models.DateField()
    cvv = models.CharField(max_length=3)
    pin = models.CharField(max_length=6)

    def __str__(self):
        return self.customer.C_fname

class Payment_Confirmation(models.Model):
    book = models.ForeignKey(booking,on_delete=models.CASCADE)
    transaction = models.CharField(max_length=16)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.book.customer.C_fname
