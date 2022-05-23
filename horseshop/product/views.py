from django.shortcuts import get_object_or_404, render

from product.models import Product, ProductInCart
from product.forms import ProductAddToCart

from category.models import Subcategory


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_to_cart_form = ProductAddToCart()
    info_add_product = None
    context = {'product': product,
               'product_to_cart_form': product_to_cart_form,
               'info_add_product': info_add_product}
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


def cart_detail(request):
    products_in_cart = ProductInCart.objects.all()
    context = {'products_in_cart': products_in_cart}
    return render(request, 'base.html', context)


def product_add_to_cart(request, product_pk):
    if request.method == 'POST':
        if form.is_valid():
            form = ProductAddToCart(request.POST)
            cleaned_data = form.cleaned_data
            count = cleaned_data['quantity']
            product = get_object_or_404(Product, pk=product_pk)
            product_to_cart = ProductInCart.objects.get_or_create(product=product)
            product_to_cart.count += count
            product_to_cart.save(update_fields=['count'])
            info_add_product = 'Product has been added to your Cart'
    context = {'info_add_product': info_add_product}
    return render(request, 'product/product_detail.html', context)
