from django.db import models


# Create your models here.
class Tbl_cat(models.Model):
    Cat_name = models.CharField(max_length=20)
    Cat_desc = models.CharField(max_length=100)
    def __str__(self):
         return self.Cat_name


class Sub_category(models.Model):
    category = models.ForeignKey(Tbl_cat, on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=30)
    des = models.CharField(max_length=30)
    def __str__(self):
      return self.sub_name