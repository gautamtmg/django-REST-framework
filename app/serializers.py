from .models import Book
from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=80)
    author = serializers.CharField(max_length=80)
    price = serializers.IntegerField(default=0)

    def create(self, validated_data):  # this validated_data comes in dictionary form
        return Book.objects.create(**validated_data)


    def update(self, instance, validated_data):
        newBook = Book(**validated_data)
        newBook.id = instance.id
        newBook.save()
        return newBook
