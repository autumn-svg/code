from rest_framework import serializers
from .models import Book

class BookListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title',)

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'