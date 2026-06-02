from django.shortcuts import render,get_object_or_404
from .serializers import BookListSerializers, BookSerializers
from .models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def index(request):
    books = Book.objects.all()
    serializer = BookListSerializers(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializers(book)
    return Response(serializer.data)
