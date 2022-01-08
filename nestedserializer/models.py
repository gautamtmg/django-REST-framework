from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    price = models.IntegerField(default=0)


    def __str__(self):
        return self.title