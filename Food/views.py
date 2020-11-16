from django.shortcuts import render
from rest_framework import viewsets,routers

from .serializers import Mealserializer
from .models import Meals
from . import views

# Create your views here.
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meals.objects.all().order_by('name')
    serializer_class = Mealserializer

    


router = routers.DefaultRouter()
router.register(r'meals', views.MealViewSet)
