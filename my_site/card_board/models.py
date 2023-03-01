from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.
class Cardinfo(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    enddata = models.CharField(max_length=200)
    picture  = models.CharField(max_length=200)
    oldlink = models.CharField(max_length=500)

    # def __str__(self):
    #     return f"{self.name},{self.price},{self.picture}"


class Kobecardinfo(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    enddata = models.CharField(max_length=200)
    picture  = models.CharField(max_length=200)
    oldlink = models.CharField(max_length=500)


class Jamescardinfo(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    enddata = models.CharField(max_length=200)
    picture  = models.CharField(max_length=200)
    oldlink = models.CharField(max_length=500)


class Jordanscardinfo(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    enddata = models.CharField(max_length=200)
    picture  = models.CharField(max_length=200)
    oldlink = models.CharField(max_length=500)