from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PovarViewSet, IngredientsListCreate, DishListCreate, DishDetail

router = DefaultRouter()
router.register(r'povars', PovarViewSet)

urlpatterns = [
    path('ingredients/', IngredientsListCreate.as_view(), name='ingredients-list-create'),
    path('dishes/', DishListCreate.as_view(), name='dishes-list-create'),
    path('dishes/<int:pk>/', DishDetail.as_view(), name='dish-detail'),
]

urlpatterns += router.urls