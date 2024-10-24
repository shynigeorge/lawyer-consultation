from django.conf import settings

# Create your models here.
from django.db import models

from ad_detil.models import Sub_category, Tbl_cat


# Create your models here.
class Tbl_adv(models.Model):
    Adv_fname = models.CharField(max_length=20)
    Adv_lname = models.CharField(max_length=20)
    Adv_email = models.EmailField(default="")
    Adv_gen = models.CharField(max_length=10, default="")
    Adv_dob = models.DateField()
    Adv_ph = models.CharField(max_length=10)
    Adv_state = models.CharField(max_length=30, default="")
    Adv_city = models.CharField(max_length=10)
    Adv_dist = models.CharField(max_length=30)
    Adv_pin = models.CharField(max_length=10)
    Adv_status = models.BooleanField()
    Adv_pass = models.CharField(max_length=20)
    Adv_image = models.ImageField(upload_to='Adv_images',null=True)
    Adv_experience = models.PositiveIntegerField(null=True)
    Adv_description = models.TextField(null=True)
    Adv_subcategory=models.ForeignKey(Sub_category, on_delete=models.CASCADE,default=1)
    Adv_category = models.ForeignKey(Tbl_cat, on_delete=models.CASCADE, default=1)
    Adv_approval=models.BooleanField(default=False)
    u = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
    Adv_join_date=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.Adv_fname
# Create your models here.

