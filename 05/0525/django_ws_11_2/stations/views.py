from django.shortcuts import render
from rest_framework import viewsets
from .models import Station
from .serializers import StationListSerializer, StationSerializer

# Create your views here.

class StationView(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return StationListSerializer
        return StationSerializer