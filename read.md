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
from django.http import JsonResponse

def bookListView(request):

    return JsonResponse({"title": " Book Title Here"})
```

### Now with serializers
> views.py
```python
from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer

def bookListView(request):
    books = Book.objects.all()
    serializers = BookSerializer(books, many=True)
    return JsonResponse(serializers.data, safe=False)
```
> In order to allow non-dict objects to be serialized set the safe parameter to False.
> Here serializer converts python object inot Json and serializers.data is in string fromat so we need to add safe=False

### To handle POST request
> view.py
```python
from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer
from django.views.decorators.csrf import csrf_exempt #it ignores csrf
from rest_framework.parsers import JSONParser

@csrf_exempt
def bookListView(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializers = BookSerializer(books, many=True)
        return JsonResponse(serializers.data, safe=False)
    elif request.method == "POST":
        jsonData = JSONParser().parse(request)
        serializers = BookSerializer(data = jsonData)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, safe=False)
        else:
            return JsonResponse(serializers.errors, safe=False)
```
> In HTTP request, we receive data as string. JSONparser().parse() helps to convert JSON content into python data types based on Content-Type header.


serializer.save() method call create() function in serializer Class (BookSerializer)