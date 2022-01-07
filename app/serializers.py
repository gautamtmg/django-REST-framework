from .models import Book
from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=80)
    author = serializers.CharField(max_length=80)
    price = serializers.IntegerField(default=0)