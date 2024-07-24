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
        fields = ['id', 'dish_name', 'dish_price', 'dish_rating', 'dish_ingredients', 'dish_povars']
    
    def validate_dish_ingredients(self, value):
        if not value:
            raise serializers.ValidationError("This field is required.")
        return value

    def validate_dish_povars(self, value):
        if not value:
            raise serializers.ValidationError("This field is required.")
        return value