from django.shortcuts import render
from django.http import HttpResponse
from products.models import Products ,Types,TypeSale

# Create your views here.
def home(request):
    queryset1 = Products.objects.select_related('TypeSale').filter(TypeSale=4);
    queryset2 = Products.objects.select_related('TypeSale').filter(TypeSale=5);
    for product in queryset1:
        product.newPrice = int((100-int(product.numSale))*product.price/100)
    context ={
        "queryset1" : queryset1,
        "queryset2" : queryset2
    }
    print(queryset1)
    return render(request, 'index.html',context)

