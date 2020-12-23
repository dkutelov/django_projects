from django.db import models
from django.core.validators import MinValueValidator

from .enums import FoodTypeEnum, MealTypeEnum


class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=360)
    price = models.DecimalField(validators=[MinValueValidator(0)],max_digits=6, decimal_places=2, default=0)
    units_on_stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False) 
    calories = models.PositiveIntegerField(default=0)
    meal_type = models.CharField(max_length=50, choices=[(mt.name, mt.value) for mt in MealTypeEnum])
    food_type = models.CharField(max_length=50, choices=[(ft.name, ft.value) for ft in FoodTypeEnum])

    def __str__(self):
        return f'{self.name}'


class MealPhoto(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    photo_url = models.URLField(max_length=200, default="ttps://res.cloudinary.com/dariku/image/upload/v1607681887/events/user-photos/user-default.jpg")
    is_default = models.BooleanField(default=False)


class Ingredients(models.Model):
    meal = models.ManyToManyField(Meal, blank=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'
