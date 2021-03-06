from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import request
from .models import Account,Customer
from django.db.models.query import EmptyQuerySet

# Create your views here.

def login(request):
    return render(request,'login.html')

def checkLogin(request):
    username = request.POST['username'];
    password = request.POST['password'];
    acc = Account.objects.filter(username=username ,password = password).values('customer_id');
    if(len(acc)==0):
        return redirect('login')
    else:
        request.session['user']=acc[0]['customer_id']
        return redirect('/')

def signup(request):
    if(request.method=='POST'):
        name = request.POST['name'];
        birthday = request.POST['birthday'];
        username = request.POST['email'];
        password = request.POST['password'];
        Customer.objects.create(name=name,birthday=birthday,email=username);
        id = Customer.objects.values('id').latest('id')
        Account.objects.create(customer_id = id['id'],username=username,password=password);
        return redirect('login')
    else:
        return render(request,'signup.html')

def logout(request):
    del request.session['user']
    return redirect('/')