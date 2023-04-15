from django.shortcuts import render
from .models import Product
# Create your views here.


def shop(request):
    products = Product.objects.order_by('-date')
    return render(request, 'shop.html', {'products': products})

def addproduct(request):
    pass
