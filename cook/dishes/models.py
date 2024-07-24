from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class Povar(models.Model):
    Povar_name = models.CharField(max_length=50)
    Povar_experience = models.IntegerField()
    Povar_rating = models.FloatField()
    Povar_age = models.IntegerField()


class Ingredients(models.Model):
    ingredient_name = models.CharField(max_length=50)
    ingredient_price = models.FloatField()
    types = (
        (0, "fish"),
        (1, "meat"),
        (2, "vegetables"),
    )
    ingredient_type = models.IntegerField(choices=types, default=0)


class Dish(models.Model):
    dish_name = models.CharField(max_length=50)
    dish_price = models.FloatField()
    dish_rating = models.FloatField()
    dish_ingredients = models.ManyToManyField(Ingredients)
    dish_povars = models.ForeignKey(Povar, on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

