from django.shortcuts import get_object_or_404, render

from product.models import Product
from product.forms import ProductAddToCart

from category.models import Subcategory




def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_to_cart_form = ProductAddToCart()
    context = {'product': product, 'product_to_cart_form': product_to_cart_form}
    return render(request, 'product/product_detail.html', context)


def product_list(request, subcategory_slug=None):
    subcategory = None
    context = {}
    subcategories = Subcategory.objects.all()
    products = Product.objects.filter(is_active=True)
    if subcategory_slug:
        subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
        products = products.filter(subcategory=subcategory)
        context = {'subcategory': subcategory, 'subcategories': subcategories,
                   'products': products}
    return render(request, 'product/product_list.html', context)


# def cart_detail(request, pk):
#     product_in_cart = ProductInCart.objects.all()
#     context={'product_in_cart': product_in_cart}
#     return render(request, 'base.html', {'cart': cart})

# def product_add_to_cart(request, product_pk):
#     # product = get_object_or_404(Product, pk=product_pk)
#     # form = ProductAddToCart(request.POST)
#     # if form.is_valid():
#     #     cleaned_data = form.cleaned_data
#     #     product_to_cart.add(product=product, quantity=cleaned_data['quantity'],
#     #              update_quantity=cleaned_data['update'])
#     # info_add_product = 'Product has been added to your Cart'
#     # context={'info_add_product': info_add_product}
#     return redirect('product:cart_detail', context)
