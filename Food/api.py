from rest_framework.response import Response
from rest_framework import generics,permissions
from .serializers import Mealserializer,CustomerSerializer
from .models import Meals,Customer

class mealsApi(generics.ListCreateAPIView):

    queryset=Meals.objects.all()
    serializer_class=Mealserializer

class CustomerApi(generics.ListCreateAPIView):
    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
