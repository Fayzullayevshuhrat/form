from django.db import models
from django.db.models import Model, CharField, IntegerField


# Create your models here.
class Product(Model):
    name=CharField(max_length=255)
    price=IntegerField()
    describtion=CharField(max_length=255)
    def __str__(self):
        return self.name