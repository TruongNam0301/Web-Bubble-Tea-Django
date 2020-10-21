from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from products.models import Products ,Types,TypeSale
from products.cart import Cart
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
def products(request):
    queryset1 = Types.objects.all();
    arr_product =[]
    for type in queryset1:
        arr = []
        queryset2 = Products.objects.select_related('Types','TypeSale').filter(Types_id= type.id)
        for product in queryset2:
            product.newPrice = int((100-int(product.numSale))*product.price/100)
            arr.append(product)
        arr_product.append(arr)
    all = zip(queryset1,arr_product)

    context ={
        'queryset1': queryset1,
        'queryset2': all
    }
    return render(request, 'products.html',context)

@csrf_exempt
def addCart(request):
    if request.is_ajax and request.method == "POST":
        id = request.POST['id'];
        quantity = request.POST['quantity']
        size = request.POST['size'];
        sugar = request.POST['sugar'];
        toppings = request.POST.getlist('toppings[]') ;
        product = {'id': id,'quantity':quantity ,'size': size,'sugar': sugar,'toppings': toppings}
        if not 'cart' in request.session:
            request.session['cart'] = {'products': [],'total_quantity': 0 ,'total_price':0}  
        cart = Cart(request.session['cart'])
        request.session['cart'] = cart.addCart(product)
        print(request.session['cart'])
        return HttpResponse(request.session['cart']['total_quantity'])

def detail(request,id):
    product = Products.objects.get(id=id);
    product.newPrice = int((100-int(product.numSale))*product.price/100)
    return render(request,'detail.html',{'product':product})
