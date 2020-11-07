from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    birthday =models.DateField()
    email = models.CharField(max_length=25,null=True)

class Account(models.Model):
    customer =  models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    username = models.CharField(max_length= 25)
    password = models.CharField(max_length=25)
   
