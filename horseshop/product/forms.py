from django import forms
# from .models import ProductInCart


# class ProductAddToCart(forms.ModelForm):
#     class Meta:
#         model = ProductInCart
#         fields = ['total_count', 'color','size']
#         labels = {
#             'total_count': 'Quantity',
#             'color': 'Color',
#             'size': 'Size'
#         }

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(0, 51)]


class ProductAddToCart(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int, initial=1)
    update = forms.BooleanField(required=False, initial=True,
                                widget=forms.HiddenInput)
