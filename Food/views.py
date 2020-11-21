from django.shortcuts import render
from rest_framework import viewsets,routers
from rest_framework.permissions import IsAdminUser
from .serializers import Mealserializer
from .models import Meals
from . import views

# Create your views here.
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meals.objects.all().order_by('name')
    serializer_class = Mealserializer
    permission_classes=[IsAdminUser]

    



