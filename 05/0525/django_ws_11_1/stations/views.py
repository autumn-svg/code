from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import LocationSerializer, CarSerializer, StationSerializer
from .models import Location, Car, Station
from rest_framework.response import Response
# Create your views here.

