from django.contrib import admin
from .models import CurrentOrders,Customer,OrderHistory,Meals,Hero
# Register your models here.

admin.site.register(CurrentOrders)
admin.site.register(Hero)

admin.site.register(Customer)
admin.site.register(Meals)

admin.site.register(OrderHistory)

