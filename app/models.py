from django.db import models
from django.db.models.base import Model

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    price = models.IntegerField(default=0)