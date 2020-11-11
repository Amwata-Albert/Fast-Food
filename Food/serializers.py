from rest_framework import serializers
from .models import CurrentOrders

class CurrentOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentOrders
        fields = ('food', 'status', 'amount' , 'address')
        # fields = ('__all__')