from django.shortcuts import render
from api.models import Restaurant
from api.serializers import RestaurantSerializer
from rest_framework import generics

# Create your views here.
class RestaurantAPIView(generics.ListCreateAPIView):
    # .objects is a manager
    # .all() is the query to get all objects
    queryset = Restaurant.objects.all() 
    serializer_class = RestaurantSerializer
