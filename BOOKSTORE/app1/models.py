from django.db import models

# Create your models here.


class Books(models.Model):
    Bname = models.CharField(max_length=20)
    Bprice = models.CharField(max_length=4)
    Bauthor = models.CharField(max_length=20)
    Bcategory = models.CharField(max_length=20)
    Bstock = models.CharField(max_length=2)
    Bqty = models.CharField(max_length=3)
    File = models.FileField(upload_to='documents',default="")
    Image = models.ImageField(upload_to='images',default="")

    def __str__(self):
        return self.Bname



