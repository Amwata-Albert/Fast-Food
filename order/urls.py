from django.urls import path
from .api import CurrentOrders, CurrentOrdersApi

urlpatterns = [
    path('api/order', CurrentOrdersApi.as_view()),
]