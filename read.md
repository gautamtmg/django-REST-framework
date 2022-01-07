# Django REST framework

### To install django REST framework

> pip install djangorestframework

### Goto settings.py and add 'rest_framework' in installed apps
```python
INSTALLED_APPS = [
   ....
    'rest_framework'
]
```
 
### Make a model
```python
from django.db.models.base import Model

class Book(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    price = models.IntegerField(default=0)
```

#### After making we need to make serializers, which helps to convert python objects into datatype that is understandable by javascript (JSON)
> serializes.py
```python
from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=80)
    author = serializers.CharField(max_length=80)
    price = serializers.IntegerField(default=0)
```


### To response a JSON file
> views.py
```python
from django.shortcuts import render
from django.http import JsonResponse

def bookListView(request):

    return JsonResponse({"title": " Book Title Here"})
```

### Now with serializers
> views.py
```python
    from django.shortcuts import render
from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer

def bookListView(request):
    books = Book.objects.all()
    serializers = BookSerializer(books, many=True)
    return JsonResponse(serializers.data, safe=False)
```
> Here serializer converts python object inot Json and serializers.data is in string fromat so we need to add safe=False