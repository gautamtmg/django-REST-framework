from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from app.models import Book
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def bookListView(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializers = BookSerializer(books, many=True)
        return Response(serializers.data)
    elif request.method == "POST":
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def bookDetailView(request, pk):

    try:
        book = Book.objects.get(pk = pk)

    except Book.DoesNotExist:
        return Response(status= 404)


    if request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = BookSerializer(book, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
