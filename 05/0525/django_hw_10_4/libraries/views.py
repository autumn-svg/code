from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from .models import Book
from .serializers import BookListSerializer, BookSerializer

# Create your views here.
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookListSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book_detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['POST'])
def book_create(request):
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def book_delete(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    if request.method == 'DELETE':
        message = {
            'delete' : f'도서 고유 번호 {book.isbn}번의 {book.title}을 삭제하였습니다.'
        }
        book.delete()
        return Response(message, status=status.HTTP_204_NO_CONTENT)


