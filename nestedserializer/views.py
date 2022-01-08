from re import search
from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def book(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def category(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
