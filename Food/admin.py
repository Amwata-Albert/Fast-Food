from django.contrib import admin
from .models import Hero
from .models import CurrentOrders,Customer,OrderHistory,Meals

# Register your models here.
admin.site.register(Hero)
admin.site.register(Customer)
admin.site.register(Meals)
admin.site.register(OrderHistory)


