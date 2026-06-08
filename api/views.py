from django.shortcuts import render
from api.models import Restaurant, Rating, Sale
from api.serializers import RestaurantSerializer, RatingSerializer
from rest_framework import generics
from django.db.models import Sum, Prefetch
from django.utils import timezone


def get_monthly_sales():
    month_ago = timezone.now() - timezone.timedelta(days=30)
    monthly_sales = Prefetch(
        'sales',
        queryset=Sale.objects.filter(datetime__gte=month_ago)
    )
    return monthly_sales

# Create your views here.
class RestaurantAPIView(generics.ListCreateAPIView):
    # .objects is a manager
    # .all() is the query to get all objects
    
    ## n+1 problem here -> 1 query for the restaurant fetch
    ## other n query for n ratings fetch
    
    # queryset = Restaurant.objects.all() 
    ## prefetch related runs 2 queries under the hood
    ## SELECT ••• FROM "api_restaurant" ORDER BY LOWER("api_restaurant"."name") ASC
    ## SELECT ••• FROM "api_rating" WHERE "api_rating"."restaurant_id" IN (22, 25, 26, 21, 27, 32, 23, 28, 29, 19, 20, 30, 31, 24) 

    # queryset = Restaurant.objects.filter(name__istartswith='c').prefetch_related('ratings', 'sales')
    
    # queryset = Restaurant.objects.prefetch_related('ratings', 'sales').filter(ratings__rating=5).annotate(total=Sum('sales__income'))
    
    ## we are limiting the prefetch_related here to only get the base queryset(here monthly sales only)
    queryset = Restaurant.objects.prefetch_related('ratings', get_monthly_sales()).filter(ratings__rating=5).annotate(total=Sum('sales__income'))
    serializer_class = RestaurantSerializer


class RatingAPIView(generics.ListCreateAPIView):
    ## select related joins the two tables and shows the data

    ## only() to select selected fields from joined table
    ## need to use carefully otherwise if we miss a field django orm will
    ## interally call another query which is not optimized
    
    queryset = Rating.objects.only('rating', 'restaurant__name').select_related('restaurant')
    serializer_class = RatingSerializer
