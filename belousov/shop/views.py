from django.shortcuts import render
from .models import Product
from .forms import ProductForm


# Create your views here.


def shop(request):
    products = Product.objects.order_by('-date')
    return render(request, 'shop.html', {'products': products})


def addproduct(request):


    add_form = ProductForm()

    data = {
        'add_form': add_form
    }

    return render(request, 'addproduct.html', data)
