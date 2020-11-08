from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Types(models.Model):
    nameType = models.CharField(max_length= 100)
    def __str__(self):
        return str(self.nameType)


class TypeSale(models.Model):
    nameTypeSale = models.CharField(max_length= 100)
    def __str__(self):
        return str(self.nameTypeSale)

class Products(models.Model):
    name = models.CharField(max_length= 100)
    price = models.IntegerField()
    image = models.FileField(upload_to="img/products_image",blank=True)
    Types = models.ForeignKey(Types , on_delete=models.CASCADE)
    TypeSale = models.ForeignKey(TypeSale , on_delete=models.CASCADE)
    numSale = models.IntegerField(default=0)
   
    
    