from django.urls import path

from .api import MealsApi

from django.urls import include, path
from rest_framework import routers
from . import views
from .api import CustomerApi


urlpatterns = [
    path('api/Meals',MealsApi.as_view()),
    path('api/customer', CustomerApi.as_view()),
]