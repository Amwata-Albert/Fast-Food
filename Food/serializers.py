<<<<<<< HEAD

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer,CurrentOrders,OrderHistory,Meals

class Mealserializer(serializers.ModelSerializer):
    class Meta:
        model= Meals
        fields= '__all__'





class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__' 

=======
from rest_framework import  serializers
from django.contrib.auth.models import User
from .models import Customer,CurrentOrders,OrderHistory,Meals

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__' 
>>>>>>> a0a3a53844208a7fcf06d0d45b96a62bbe87b56a
