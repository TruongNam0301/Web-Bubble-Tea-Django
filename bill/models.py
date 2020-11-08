from products.views import products
from django.db import models
from User.models import Customer
from products.models import Products 
from django.db.models.deletion import CASCADE
# Create your models here.
class Bill(models.Model):
    customer =  models.ForeignKey(Customer , on_delete=models.CASCADE)
   

class BillDetail(models.Model):
    bill =  models.ForeignKey(Bill , on_delete=models.CASCADE)
    products =  models.ForeignKey(Products , on_delete=models.CASCADE)
    size = models.CharField(max_length= 25)
    sugar = models.CharField(max_length= 25)
    quantity = models.IntegerField()
    topping = models.CharField(max_length= 50)
    address = models.CharField(max_length= 50)
    phone = models.IntegerField()
    def __str__(self):
        return str(self.products)