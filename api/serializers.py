from rest_framework import serializers
from api.models import Restaurant, Rating, Sale

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'income', 'datetime']


class RestaurantSerializer(serializers.ModelSerializer):
    # ratings = RatingSerializer(many=True, read_only=True)
    sales = SaleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'sales']
        
        
class RatingSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(source='restaurant.name')
    
    class Meta:
        model = Rating
        fields = ['id', 'restaurant_name', 'rating']
    
    
    # adding custom validation
    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 to 5")
        return value
