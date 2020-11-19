from rest_framework import  serializers
from django.contrib.auth.models import User
from .models import CurrentOrders

class CurrentOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentOrders
        fields = '__all__' 