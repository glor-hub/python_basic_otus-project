from django.shortcuts import get_object_or_404, render
from django.forms import formset_factory
from product.models import Product, ProductInCart
from product.forms import ProductAddToCart

from category.models import Subcategory


def product_detail(request, pk):
    context = {}
    product = get_object_or_404(Product, pk=pk)
    product_to_cart_form = ProductAddToCart()
    add_operation_success = ''
    if request.method == 'POST':
        form = ProductAddToCart(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            count = int(cleaned_data['quantity'])
            product = get_object_or_404(Product, pk=pk)
            ProductInCart.objects.get_or_create(product=product)
            product_to_cart = get_object_or_404(ProductInCart, product=product)
            product_to_cart.total_count += count
            product_to_cart.save()
            add_operation_success = 'Product has been added to your Cart'
    product_in_cart = ProductInCart.objects.all()
    context = {'product': product, 'product_in_cart': product_in_cart,
               'product_to_cart_form': product_to_cart_form,
               'add_operation_success': add_operation_success}
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
    context = {}
    total_count = 0
    total_cost=0
    products_in_cart = ProductInCart.objects.all()
    for product in products_in_cart:
        total_count += product.total_count
        total_cost += product.total_price
    context = {'products_in_cart': products_in_cart, 'total_count': total_count,
               'total_cost': total_cost
               }
    return render(request, 'product/cart_detail.html', context)

def cart_add_item(request, pk):
    product=get_object_or_404(ProductInCart,pk=pk)
    quantity = product.total_count
    quantity+=1
    product.total_count=quantity
    product.save()
    return cart_detail(request)

def cart_reduce_item(request, pk):
    product=get_object_or_404(ProductInCart,pk=pk)
    quantity = product.total_count
    quantity-=1
    if quantity==0:
        product.delete()
        return cart_detail(request)
    product.total_count=quantity
    product.save()
    return cart_detail(request)


def cart_delete_item(request, pk):
    product=get_object_or_404(ProductInCart,pk=pk)
    product.delete()
    return cart_detail(request)
