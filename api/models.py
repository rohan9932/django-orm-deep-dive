from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.functions import Lower

# Restaurant, User, Rating

class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        BANGLADESHI = 'BN', 'Bangladeshi'
        INDIAN = 'IN', 'Indian' # db stored value, frontend read value
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GR', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fastfood'
        OTHERS = 'OT', 'Others'  

    name = models.CharField(max_length=100)
    website = models.URLField(default="")
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)
    
    class Meta:
        ordering = [Lower('name')]
        get_latest_by = 'date_opened'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        print(self._state.adding) # checking if a obj is added in the model
        # for eg. it can be helpful in a scenario where when use login for the first time
        # they get an email in their inbox
        super().save(*args, **kwargs)


class Staff(models.Model):
    name = models.CharField(max_length=128)
    restaurants = models.ManyToManyField(Restaurant, related_name='staffs', through='StaffRestaurant')
    
    def __str__(self):
        return self.name
    

class StaffRestaurant(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    salary = models.FloatField(null=True, blank=True)
    


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"Rating: {self.rating}"
    

class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='sales')
    income = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)
