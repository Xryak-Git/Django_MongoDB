from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.views.generic import UpdateView, DetailView, DeleteView


# Create your views here.
class DetailProduct(DetailView):
    model = Product
    template_name = 'detail_view.html'

    context_object_name = 'product'


class UpdateProduct(UpdateView):
    model = Product
    template_name = 'update-product.html'

    form_class = ProductForm


class DeleteProduct(DeleteView):
    model = Product
    template_name = 'delete-product.html'

    success_url = '/shop/'


def shop(request):
    products = Product.objects.order_by('date')
    return render(request, 'shop.html', {'products': products})


def add_product(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop')
        else:
            error = 'Чо-то неправильно'

    add_form = ProductForm()

    data = {
        'add_form': add_form
    }

    return render(request, 'add-product.html', data)
