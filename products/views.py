from django.shortcuts import render
from products.models import Products ,Types,TypeSale
# Create your views here.
def products(request):
    queryset1 = Types.objects.all();
    arr_product =[]
    for type in queryset1:
        arr = []
        queryset2 = Products.objects.select_related('Types','TypeSale').filter(Types_id= type.id)
        for product in queryset2:
            product.newPrice = int((100-int(product.TypeSale.numSale))*product.price/100)
            arr.append(product)
        arr_product.append(arr)
    all = zip(queryset1,arr_product)

    context ={
        'queryset1': queryset1,
        'queryset2': all
    }
    return render(request, 'products.html',context)

