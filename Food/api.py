from rest_framework.response import Response
from rest_framework import generics,permissions
from .serializers import Mealserializer,CustomerSerializer,CurrentOrdersSerializer,OrderHistorySerializer
from .models import Meals,Customer,CurrentOrders,OrderHistory


class OrderHistoryApi(generics.ListCreateAPIView):

    queryset=OrderHistory.objects.all()
    serializer_class=OrderHistorySerializer

class OrderHistoryDetailApi(generics.RetrieveUpdateDestroyAPIView):

    queryset=OrderHistory.objects.all()
    serializer_class=OrderHistorySerializer

class mealsApi(generics.ListCreateAPIView):

    queryset=Meals.objects.all()
    serializer_class=Mealserializer

class mealsDetailApi(generics.RetrieveUpdateDestroyAPIView):

    queryset=Meals.objects.all()
    serializer_class=Mealserializer

class CustomerApi(generics.ListCreateAPIView):
    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CurrentOrdersApi(generics.ListCreateAPIView):
    
    queryset = CurrentOrders.objects.all()
    serializer_class = CurrentOrdersSerializer

class CurrentOrderDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = CurrentOrders.objects.all()
    serializer_class = CurrentOrdersSerializer



