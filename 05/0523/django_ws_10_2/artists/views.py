from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from .models import Artist
from .serializers import ArtistSerializer, ArtistListSerializer

# Create your views here.
@api_view(['GET','POST'])
def artist_list_or_create(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ArtistSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def artist_detail(request, pk):
    if request.method == 'GET':
        artist = get_object_or_404(Artist, pk=pk)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)