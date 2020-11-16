from django.contrib import admin
<<<<<<< HEAD
from .models import Hero


# Register your models here.
admin.site.register(Hero)
=======
from .models import CurrentOrders,Customer,OrderHistory,Meals
# Register your models here.

admin.site.register(Customer)
admin.site.register(CurrentOrders)
admin.site.register(Meals)
admin.site.register(OrderHistory)
>>>>>>> a0a3a53844208a7fcf06d0d45b96a62bbe87b56a
