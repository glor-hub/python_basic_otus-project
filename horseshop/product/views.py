from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView

from product.models import Product
from category.models import Subcategory


class ProductDetailView(DetailView):
    model = Product

def product_list(request, subcategory_slug=None):
    subcategory= None
    context={}
    subcategories = Subcategory.objects.all()
    products = Product.objects.filter(is_active=True)
    if subcategory_slug:
        subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
        products = products.filter(subcategory=subcategory)
        context={'subcategory': subcategory, 'subcategories': subcategories,
                   'products': products}
    return render(request, 'product/product_list.html',context)
