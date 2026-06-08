from django.urls import path
from api import views

urlpatterns = [
    path('restaurants/', views.RestaurantAPIView.as_view(), name='restaurant_list'),
    path('ratings/', views.RatingAPIView.as_view(), name='ratings')
] 
