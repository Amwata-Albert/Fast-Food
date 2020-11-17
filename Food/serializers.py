from rest_framework import serializers
from .models import CurrentOrders,Meals
from django.contrib.auth.models import User
class CurrentOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentOrders
        # fields = ('food', 'status', 'amount' , 'address')
        fields = ('__all__')

      




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

