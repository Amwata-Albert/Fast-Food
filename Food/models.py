from django.db import models


# Create your models here.

class Meals(models.Model):
	food_id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=50,null=True)
	price=models.IntegerField(null=True)
	photo=models.CharField(max_length=100,null=True)
	category=models.CharField(max_length=20,null=True)

	def __str__(self):
		return self.meals

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name        