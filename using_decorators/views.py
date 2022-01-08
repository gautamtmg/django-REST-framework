from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from app.models import Book
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView

# Function BASED View

# @api_view(['GET', 'POST'])
# def bookListView(request):
#     if request.method == "GET":
#         books = Book.objects.all()
#         serializers = BookSerializer(books, many=True)
#         return Response(serializers.data)
#     elif request.method == "POST":
#         serializer = BookSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def bookDetailView(request, pk):

#     try:
#         book = Book.objects.get(pk = pk)

#     except Book.DoesNotExist:
#         return Response(status= 404)


#     if request.method == "DELETE":
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == "GET":
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = BookSerializer(book, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

from django.http import Http404

# classed Based View
class BookListView(APIView):
    
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BookDetailView(APIView):

    def get_book(self,pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        book = self.get_book(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book = self.get_book(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        book = self.get_book(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
