from .api import MealsApi,CustomerApi
from django.urls import include, path
from rest_framework import routers
from . import views



urlpatterns = [
    path('api/Meals',MealsApi.as_view()),
    path('api/customer', CustomerApi.as_view()),
]
