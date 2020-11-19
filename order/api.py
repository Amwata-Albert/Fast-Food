from rest_framework.response import Response
from rest_framework import generics,permissions

from .serializers import CurrentOrdersSerializer
from .models import CurrentOrders

class CurrentOrdersApi(generics.ListCreateAPIView):
    
    queryset = CurrentOrders.objects.all()
    serializer_class = CurrentOrdersSerializer