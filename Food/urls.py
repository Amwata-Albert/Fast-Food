from .api import mealsApi,CustomerApi,CustomerDetailApi,CurrentOrdersApi,CurrentOrderDetailApi,mealsDetailApi,OrderHistoryApi,OrderHistoryDetailApi
from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('api/meals',mealsApi.as_view()),
    path('api/meals/<int:pk>',mealsDetailApi.as_view()),
    path('api/orderhistory',OrderHistoryApi.as_view()),
    path('api/orderhistory/<int:pk>',OrderHistoryDetailApi.as_view()),
    path('api/customer', CustomerApi.as_view()),
    path('api/customer/<int:pk>', CustomerDetailApi.as_view()),
    path('api/currentorder', CurrentOrdersApi.as_view()),
    path('api/currentorder/<int:pk>', CurrentOrderDetailApi.as_view()),
]

