from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    product = Product.objects.all()
    return render(request,'index.html',{'product':product}) 

def product(request,pk):
    product = Product.objects.get(id=pk)
    products = Product.objects.all()
    context = {'product':product,'products':products}
    return render(request,'item.html',context)