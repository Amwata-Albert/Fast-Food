from rest_framework.response import Response
from rest_framework import generics,permissions

from .serializers import Mealserializer
from .models import Meals

class MealsApi(generics.ListCreateAPIView):

    queryset=Meals.objects.all()
    serializer_class=Mealserializer