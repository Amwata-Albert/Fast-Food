from .api import mealsApi,CustomerApi,CustomerDetailApi
from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('api/meals',mealsApi.as_view()),
    path('api/customer', CustomerApi.as_view()),
    path('api/customer/<int:pk>', CustomerDetailApi.as_view()),
]

