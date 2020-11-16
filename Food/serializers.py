
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

