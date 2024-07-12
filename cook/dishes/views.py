from django.shortcuts import render

# Create your views here.
from .models import Povar, Dish, Ingredients
from rest_framework import permissions, viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
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


class DishListCreate(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)