from rest_framework.response import Response
from rest_framework import generics,permissions


from .serializers import Mealserializer
from .models import Meals,CurrentOrders

class MealsApi(generics.ListCreateAPIView):

    queryset=Meals.objects.all()
    serializer_class=Mealserializer

from .serializers import CustomerSerializer
from .models import Customer

class CustomerApi(generics.ListCreateAPIView):
    
    queryset = Customer.objects.all()

    serializer_class = CustomerSerializer

    serializer_class = CustomerSerializer

