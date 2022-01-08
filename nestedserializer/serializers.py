from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Book, Category



class CategorySerializer(serializers.ModelSerializer):
    # books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Book
        fields = "__all__"