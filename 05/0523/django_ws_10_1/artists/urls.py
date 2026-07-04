from django.urls import path, include
from . import views

app_name = 'artists'

urlpatterns = [
    path('artists/', views.create_singer, name='create_singer'),
]
