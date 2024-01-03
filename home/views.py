from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    product = Product.objects.all()
    return render(request,'index.html',{'product':product}) 

def product(request,pk):
    product = Product.objects.get(id=pk)
    products = Product.objects.all()[4:]
    context = {'product':product,'products':products}
    return render(request,'item.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        item = order.orderitem_set.all()
    else:
        item = []
        order = {'get_cart_total':0,'get_cart_items':0}
    return render(request,'cart.html',{'items':item ,'order':order})

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        item = order.orderitem_set.all()
    else:
        item = []
        order = {'get_cart_total':0,'get_cart_items':0}
    return render(request,'checkout.html',{'items':item ,'order':order})

def thanks(request):
    return render(request,'thanks.html')

def register(request):
     return render(request,'login.html')

def forgotpass(request):
    return render(request,'forgot_pass.html')
