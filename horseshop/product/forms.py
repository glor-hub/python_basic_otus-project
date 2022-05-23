from django import forms
from .models import ProductInCart


class ProductAddToCart(forms.ModelForm):
    class Meta:
        model = ProductInCart
        fields = ['total_count', 'color','size']
        labels = {
            'total_count': 'Quantity',
            'color': 'Color',
            'size': 'Size'
        }
