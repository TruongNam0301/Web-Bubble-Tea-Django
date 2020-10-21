from django.core import serializers

class Cart(object):
    def __init__(self, session):
        self.products= session['products']
        self.total_quantity= session['total_quantity']
        self.total_price = session['total_price']
    def addCart(self,product):
        x=1
        for i in range(len(self.products)):
            if self.products[i]['id'] == product['id'] and self.products[i]['size'] ==product['size'] and self.products[i]['sugar'] ==product['sugar'] and self.products[i]['toppings'] ==product['toppings']:
                self.products[i]['quantity'] = int( self.products[i]['quantity']) + int(product['quantity'])
                x=0
                break
        if (x==1):
            self.products.append(product)
        self.total_quantity = self.total_quantity+int(product['quantity'])
        return self.__dict__

