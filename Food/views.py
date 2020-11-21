from django.shortcuts import render
from rest_framework import viewsets,routers
from rest_framework.permissions import IsAdminUser
from .serializers import Mealserializer
from .models import Meals
from . import views

# Create your views here.
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meals.objects.all().order_by('name')
    serializer_class = Mealserializer
    permission_classes=[IsAdminUser]

    

# class CurrentOrders(APIView):
#     def get(self, request, format=None):
#         all_CurrentOrder = CurrentOrder.objects.all()
#         serializers = CurrentOrdersSerializer(all_CurrentOrder, many=True)
#         return Response(serializers.data)

# class CurrentOrders(APIView):

#     def post(self, request, format=None):
#         serializers = CurrentOrdersSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  
