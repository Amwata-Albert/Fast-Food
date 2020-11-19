from django.urls import path
from .api import CustomerApi,CustomerDetailApi

urlpatterns = [
    path('api/customer', CustomerApi.as_view()),
    path('api/customer/<int:pk>', CustomerDetailApi.as_view()),
]