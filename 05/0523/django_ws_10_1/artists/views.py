from django.shortcuts import render
from rest_framework import status
from .serializers import ArtistSerializer
from .models import Artist
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def create_singer(request):
    if request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
