from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .models import CurrentOrders
from rest_framework import status
from .serializers import CurrentOrdersSerializer

class CurrentOrders(APIView):
    def get(self, request, format=None):
        all_CurrentOrder = CurrentOrder.objects.all()
        serializers = CurrentOrdersSerializer(all_CurrentOrder, many=True)
        return Response(serializers.data)

class CurrentOrders(APIView):

    def post(self, request, format=None):
        serializers = CurrentOrdersSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)        