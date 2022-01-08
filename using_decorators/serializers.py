from django.db.models import fields
from app.models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book

        # fields = ['tittle', 'author']     Only selected fields data will be shown
        # Whicf field you wan to serialize
        fields = '__all__'