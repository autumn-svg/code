from django.urls import path, include
from . import views

app_name = 'libraries'

urlpatterns = [
    path('libraries/', views.index, name='index'),
    path('libraries/<int:pk>/', views.detail, name='detail'),
]