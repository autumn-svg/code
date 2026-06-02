from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from .models import Artist
from .serializers import ArtistSerializer, ArtistListSerializer, ArtistUpdateSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def artist_list_or_create(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(pk=artist_pk)
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ArtistUpdateSerializer(artist, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    if request.method == 'PUT':
        serializer = ArtistUpdateSerializer(artist, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
@api_view(['DELETE'])
def delete(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    if request.method == 'DELETE':
        message = {
            'delete' : f'등록 번호 {artist.pk}번의 {artist.name}을 삭제하였습니다.'
        }
        artist.delete()
        return Response(message, status=status.HTTP_204_NO_CONTENT)
        