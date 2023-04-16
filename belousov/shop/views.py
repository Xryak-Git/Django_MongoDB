from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


# Create your views here.


def shop(request):
    products = Product.objects.order_by('-date')
    return render(request, 'shop.html', {'products': products})




def addproduct(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop')
        else:
            error = 'Чо-то неправильно'



    add_form = ProductForm()

    data = {
        'add_form': add_form
    }

    return render(request, 'addproduct.html', data)
