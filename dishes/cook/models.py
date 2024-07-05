from django.db import models

# Create your models here.
class Povar(models.Model):
    Povar_name = models.CharField(max_length=50)
    Povar_experience = models.IntegerField()
    Povar_rating = models.FloatField()



class Ingredients(models.Model):
    ingredient_name = models.CharField(max_length=50)
    ingredient_price = models.FloatField()
    types = (
        (0, "None")
        (1, "fish"),
        (2, "meat"),
        (3, "vegetables"),
    )
    ingredient_type = models.IntegerField(choices=types, default=0)

class Dish(models.Model):
    dish_name = models.CharField(max_length=50)
    dish_price = models.FloatField()
    dish_rating = models.FloatField()
    dish_ingredients = models.ManyToManyField(Ingredients)
    dish_povars = models.ManyToManyField(Povar)