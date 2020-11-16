<<<<<<< HEAD
from .api import MealsApi,CustomerApi
from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('api/Meals',MealsApi.as_view()),
    path('api/customer', CustomerApi.as_view()),
]

    
=======
from django.urls import path
from .api import CustomerApi

urlpatterns = [
    path('api/customer', CustomerApi.as_view()),
]
>>>>>>> a0a3a53844208a7fcf06d0d45b96a62bbe87b56a
