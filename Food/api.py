from rest_framework.response import Response
from rest_framework import generics,permissions

from .serializers import CustomerSerializer
from .models import Customer

class CustomerApi(generics.ListCreateAPIView):
    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer