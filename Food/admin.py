from django.contrib import admin
from .models import CurrentOrders,Customer,OrderHistory,Meals
# Register your models here.

admin.site.register(Customer)
admin.site.register(CurrentOrders)
admin.site.register(Meals)
admin.site.register(OrderHistory)