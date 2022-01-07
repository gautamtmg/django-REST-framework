from django.shortcuts import render
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
        serializer = BookSerializer(data = jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)