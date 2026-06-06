from api.models import Restaurant, Rating, Sale
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from pprint import pprint

def run():
    # restaurant = Restaurant() # instance (obj) of restaurant
    # restaurant.name = 'My Italian Restaurant'
    # restaurant.latitude = 56.2
    # restaurant.longitude = 58.2
    # restaurant.date_opened = timezone.now()
    # restaurant.restaurant_type = restaurant.TypeChoices.ITALIAN

    # restaurant.save() # save the object

    # django querysets are lazily evaluated
    # that means main sql query won't be run if restaurants is not used anywhere
    # restaurants = Restaurant.objects.all() 
    # # print(restaurants) 
    # print(connection.queries) 


    # # restaurant = Restaurant.objects.first() 
    # restaurant = Restaurant.objects.last()  
    # print(restaurant) 
    # print(connection.queries) 

    # # getting 2nd restaurant
    # restaurant2nd = Restaurant.objects.all()[1]
    # print(restaurant2nd)
    # print(connection.queries) 


    # # Object save .create()
    # Restaurant.objects.create(
    #     name="Pizza Shop",
    #     latitude=50.5,
    #     longitude=50.5,
    #     date_opened=timezone.now(),
    #     restaurant_type=Restaurant.TypeChoices.ITALIAN
    # )
    
    # print(connection.queries)

    # print(Restaurant.objects.count())
    # print(connection.queries)

    # restaurant = Restaurant.objects.first()
    # user = User.objects.first()

    # Rating.objects.create(
    #     user=user,
    #     restaurant=restaurant,
    #     rating=3
    # )

    # print(Rating.objects.filter(rating=3))
    # print(Rating.objects.exclude(rating__gte=2))
    # print(connection.queries)


    # # change value in db
    # restaurant = Restaurant.objects.first() 
    # restaurant.name = "Edited named Restaurant"
    # restaurant.save()

    # pprint(connection.queries)

    # rating = Rating.objects.first()
    # print(rating.restaurant)
    # pprint(connection.queries)

    # foreignkey model have access to a manager to access backword connection
    # restaurant = Restaurant.objects.first()
    # # print(restaurant.rating_set.all())
    # print(restaurant.ratings.all()) # as we ovverriden related_name
    # pprint(connection.queries)


    # # sales data
    # Sale.objects.create(
    #     restaurant=Restaurant.objects.first(),
    #     income=2.33,
    #     datetime=timezone.now()
    # )
    # Sale.objects.create(
    #     restaurant=Restaurant.objects.first(),
    #     income=3.33,
    #     datetime=timezone.now()
    # )
    # Sale.objects.create(
    #     restaurant=Restaurant.objects.first(),
    #     income=4.33,
    #     datetime=timezone.now()
    # )
    # Sale.objects.create(
    #     restaurant=Restaurant.objects.first(),
    #     income=5.33,
    #     datetime=timezone.now()
    # )

    user = User.objects.first()
    restaurant = Restaurant.objects.first()

    rating, created = Rating.objects.get_or_create( # tuple (data, boolean) -> True means obj created
        restaurant=restaurant,
        user=user,
        rating=4
    ) 


    pprint(connection.queries)
