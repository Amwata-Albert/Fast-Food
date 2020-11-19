from django.db import models

# Models
class Customer(models.Model):
	user_id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=100,null=True)
	password=models.CharField(max_length=100,null=True)
	email=models.EmailField(max_length=254)
	contact=models.CharField(max_length=20,null=True)

	def __str__(self):
		return self.name

class Meals(models.Model):
	food_id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=50,null=True)
	price=models.IntegerField(null=True)
	photo=models.CharField(max_length=100,null=True)
	category=models.CharField(max_length=20,null=True)

	def __str__(self):
		return self.name

class CurrentOrders(models.Model):
	food=models.ForeignKey(Meals,null=True,on_delete=models.PROTECT)
	quantity=models.IntegerField(null=True)
	order_id=models.IntegerField(primary_key=True)
	user=models.ForeignKey(Customer,null=True,on_delete=models.PROTECT)
	status=models.CharField(max_length=20,null=True)
	order_timestamp=models.DateTimeField(null=True)
	amount=models.IntegerField(null=True)
	address=models.TextField(null=True)

	def place_order(self):
		self.order_timestamp=timezone.now()
		self.save()

class OrderHistory(models.Model):
	food=models.ForeignKey(Meals,null=True,on_delete=models.PROTECT)
	quantity=models.IntegerField(null=True)
	order_id=models.IntegerField(null=True)
	user=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
	status=models.CharField(max_length=20,null=True)
	order_timestamp=models.DateTimeField(null=True)
	amount=models.IntegerField(null=True)
