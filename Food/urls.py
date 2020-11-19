from django.urls import path
from .api import CustomerApi

urlpatterns = [
    path('api/customer', CustomerApi.as_view()),
]