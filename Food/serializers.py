from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Meals

class Mealserializer(serializers.ModelSerializer):
    class Meta:
        model= Meals
        fields= '__all__'