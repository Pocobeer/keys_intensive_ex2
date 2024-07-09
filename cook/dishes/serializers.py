from .models import Povar, Dish, Ingredients

from rest_framework import serializers

class PovarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Povar
        fields = '__all__'

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'