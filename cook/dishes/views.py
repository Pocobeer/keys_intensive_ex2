from django.shortcuts import render

# Create your views here.
from .models import Povar, Dish, Ingredients
from rest_framework import permissions, viewsets, generics, views
from .serializers import PovarSerializer, DishSerializer, IngredientsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class PovarViewSet(viewsets.ModelViewSet):
    queryset = Povar.objects.all()
    serializer_class = PovarSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        token = self.request.query_params.get('token')
        if token:
            user = TokenAuthentication().authenticate_credentials(token.encode())
            self.request.user = user
        return super().get_queryset()


class IngredientsListCreate(generics.ListCreateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = [IsAuthenticated]


class DishListCreate(views.APIView):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        dish = self.request.dish
        return dish.objects.all()
    def get_serializer_class(self):
        return self.serializer_class
    def post(self, request):
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.response(serializer.data)
        else:
            return self.response(serializer.errors)


class DishDetail(views.APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Dish.objects.get(pk=pk)
        except Dish.DoesNotExist:
            return None

    def get(self, request, pk):
        dish = self.get_object(pk)
        serializer = DishSerializer(dish)
        return self.response(serializer.data)
    
    def delete(self, request, pk):
        dish = self.get_object(pk)
        dish.delete()
        return self.response()
    


for user in User.objects.all():
    Token.objects.get_or_create(user=user)