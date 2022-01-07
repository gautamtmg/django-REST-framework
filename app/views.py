from django.shortcuts import render
from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer

def bookListView(request):
    books = Book.objects.all()
    serializers = BookSerializer(books, many=True)
    return JsonResponse(serializers.data, safe=False)