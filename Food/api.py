from rest_framework.response import Response
from rest_framework import generics,permissions

<<<<<<< HEAD
from .serializers import Mealserializer
from .models import Meals

class MealsApi(generics.ListCreateAPIView):

    queryset=Meals.objects.all()
    serializer_class=Mealserializer
=======
from .serializers import CustomerSerializer
from .models import Customer

class CustomerApi(generics.ListCreateAPIView):
    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
>>>>>>> a0a3a53844208a7fcf06d0d45b96a62bbe87b56a
