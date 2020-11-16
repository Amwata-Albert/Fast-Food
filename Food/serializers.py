<<<<<<< HEAD
from rest_framework import serializers
from .models import CurrentOrders

class CurrentOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentOrders
        fields = ('food', 'status', 'amount' , 'address')
        # fields = ('__all__')

      
=======

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Meals

class Mealserializer(serializers.ModelSerializer):
    class Meta:
        model= Meals
        fields= '__all__'

from rest_framework import  serializers
from django.contrib.auth.models import User
from .models import Customer,CurrentOrders,OrderHistory,Meals

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer

        fields = '__all__' 


        fields = '__all__' 

>>>>>>> 055822a2c06e5d63d05911cb15d615bba85508e9
