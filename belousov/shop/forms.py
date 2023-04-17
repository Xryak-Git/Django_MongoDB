from .models import Product
from django.forms import ModelForm, TextInput, NumberInput, DateTimeInput


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'date', 'image']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Название'
            }),
            'price': NumberInput(attrs={
                'placeholder': 'Цена'
            }),
            'date': DateTimeInput(attrs={
                'placeholder': 'Дата'
            }),
        }

