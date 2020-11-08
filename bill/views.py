from products.views import products
from django.shortcuts import render,redirect
from django.http import HttpResponse
from products.models import Products
from .models import Bill,BillDetail
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def cart(request):
    if 'cart' not in request.session:
        cart ={'products': []}
    else:
        cart=request.session['cart'] 
    products =[]
    dem=0
    total =0
    for item in cart['products']:
        id = item['id']
        product =Products.objects.values('name','image','price','numSale').get(id=id)
        product['quantity']=item['quantity']
        product['size']=item['size']
        product['sugar']=item['sugar']
        product['toppings']=item['toppings']
        product['stt']=dem
        product['price'] =int((100-int(product['numSale']))*product['price']/100)
        products.append(product)
        dem=dem+1
        total = total + product['price']
    
    return render(request,'cart.html',{'products':products,'total':total});

@csrf_exempt
def deleteCart(request):
    stt = int(request.POST['stt']);
    cart=request.session['cart']
    quantity =  int(cart['products'][stt]['quantity'])
    cart['total_quantity'] = cart['total_quantity'] - quantity
    cart['products'].pop(stt)
    request.session['cart']=cart
    return HttpResponse(request.session['cart']['total_quantity'])

def order(request):
    cart = request.session['cart']
    user = request.session['user']
    Bill.objects.create(customer_id=user)
    idBill = Bill.objects.values('id').latest('id')
    for item in cart['products']:
        topping = ""
        for x in item['toppings']:
            topping = topping+x
        BillDetail.objects.create(bill_id=idBill['id'],products_id=item['id'],size=item['size'],sugar=item['sugar'],quantity=item['quantity'],topping=topping,address=request.POST['address'],phone=request.POST['phone'])
    del request.session['cart']
    return redirect('/cart')
