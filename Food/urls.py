from django.urls import path
from .api import MealsApi


urlpatterns = [
    path('api/Meals',MealsApi.as_view())
]