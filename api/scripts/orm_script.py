from api.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from pprint import pprint
from django.db.models.functions import Lower, Upper
from django.db.models.aggregates import Count
import random

def run():
    ################ CREATE and READ #################
    
    
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

    # user = User.objects.first()
    # restaurant = Restaurant.objects.first()

    # rating, created = Rating.objects.get_or_create( # tuple (data, boolean) -> True means obj created
    #     restaurant=restaurant,
    #     user=user,
    #     rating=4
    # ) 


    # pprint(connection.queries)
    
    
    
    ################### UPDATE and DELETE #####################
    # restaurant = Restaurant.objects.first()
    # print(restaurant.name)
    
    # restaurant.name = 'My Bangladeshi Restaurant'
    # restaurant.save(update_fields=['name']) # only update name field
    
    # print(restaurant.name)
    
    # print(connection.queries)
    
    
    # update all fields once
    # restaurant = Restaurant.objects.filter(name__contains='Bangladesh') # __contains is a lookup
    # restaurants = Restaurant.objects.all()
    # print(
    #     restaurants.update(
    #         date_opened=timezone.now() - timezone.timedelta(700), # updates all restaurant's timezone at once
    #         website='www.test.com'
    #     )
    # )
    # # print(restaurant)
    # print(connection.queries)

    
    ## Delete
    # restaurant = Restaurant.objects.all()[1]
    # print(restaurant.delete())
    # Restaurant.objects.all().delete()
    
    
    # pprint(Restaurant.objects.filter(restaurant_type=Restaurant.TypeChoices.CHINESE))
    # pprint(Restaurant.objects.filter(restaurant_type=Restaurant.TypeChoices.CHINESE, name__startswith='C'))
    
    # check_types = [Restaurant.TypeChoices.CHINESE, Restaurant.TypeChoices.INDIAN, Restaurant.TypeChoices.MEXICAN]
    
    # restaurant = Restaurant.objects.filter(restaurant_type__in=check_types)
    # restaurant = Restaurant.objects.exclude(restaurant_type__in=check_types)
    
    # restaurant = Restaurant.objects.filter(longitude__lt=0)
    # pprint(restaurant)
    
    
    # sales = Sale.objects.select_related('restaurant').filter(income__range=(50, 60))
    # print([[sale.restaurant.name, float(sale.income)] for sale in sales])

    # r = Restaurant.objects.first()
    # r.name = r.name.lower()
    # r.save()
    
    # # restaurants = Restaurant.objects.order_by('-name') # minus means desc (case sensitive)
    
    # # solution here is to apply lowercase in db
    
    # # restaurants = Restaurant.objects.order_by(Lower('name')) # case insensitive now
    # restaurants = Restaurant.objects.all() # now  called by default ordering set in Meta class
    # print(restaurants)

    # # give use sales list by latest ones on top
    # sales = Sale.objects.order_by('-datetime')[:5]
    # print(sales)
    
    
    # restaurant = Restaurant.objects.earliest('date_opened') # just convenience function
    # restaurant2 = Restaurant.objects.latest()
    # print(restaurant, restaurant2)
    
    
    # print(Rating.objects.filter(restaurant__name__startswith='C'))
    
    
    # sales = Sale.objects.filter(restaurant__restaurant_type=Restaurant.TypeChoices.CHINESE)
    # print(sales)
     
    # pprint(connection.queries)
    
    
    ## add, all, count, remove, set, clear, create, filter, order_by
    
    # staff, created = Staff.objects.get_or_create(name='John Wick')    
    # print(staff)
    # print(type(staff.restaurants)) # many related manager
    
    # staff.restaurants.add(Restaurant.objects.first(), Restaurant.objects.all()[1])
    
    # staff.restaurants.clear()
    
    # staff.restaurants.set(Restaurant.objects.all()[:5])
    
    # print(staff.restaurants.filter(restaurant_type=Restaurant.TypeChoices.INDIAN))
    
    # print(staff.restaurants.count())
    
    # staff.restaurants.remove(Restaurant.objects.first())
    
    # print(staff.restaurants.all())
    
    
    # restaurant = Restaurant.objects.get(pk=27)
    # print(restaurant.staffs.all())
    
    # restaurant = Restaurant.objects.first()
    # restaurant2 = Restaurant.objects.last()
    
    # staff, created = Staff.objects.get_or_create(name='John Wick')
    
    # StaffRestaurant.objects.create(
    #     staff=staff, restaurant=restaurant, salary=28_000
    # )
    # StaffRestaurant.objects.create(
    #     staff=staff, restaurant=restaurant2, salary=24_000
    # )
    
    # staff_restaurants = StaffRestaurant.objects.filter(staff=staff)
    # for s in staff_restaurants:
    #     print(s.salary)
    
    # staff.restaurants.clear()
    
    # staff.restaurants.add(restaurant, through_defaults={'salary': 28_000})

    
    # staff.restaurants.set(
    #     Restaurant.objects.all()[:10],
    #     through_defaults={'salary': random.randint(20_000, 80_000)}
    # )




    ####################### Data Aggregation and Annotation #################################


    # restaurant = Restaurant.objects.values('name', 'date_opened')
    # print(restaurant)

    # print(connection.queries)

    # # db functions
    # restaurant_up = Restaurant.objects.values(name_upper=Upper('name'))
    # print(restaurant_up)

    # print(connection.queries)
    

    # # foreign key with values()
    # rating_details = Rating.objects.filter(
    #     restaurant__restaurant_type=Restaurant.TypeChoices.ITALIAN
    # ).values(
    #     'restaurant__name', 'rating'
    # )

    # print(rating_details)

    # # value list 
    # restaurant_names = Restaurant.objects.values_list('name', flat=True)
    # print(restaurant_names)


    # Aggregation
    print(Restaurant.objects.filter(name__istartswith='p').count())
    print(Restaurant.objects.aggregate(Count('id')))
    print(connection.queries)