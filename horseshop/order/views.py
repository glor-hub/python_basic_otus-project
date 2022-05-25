from django.shortcuts import render

from order.models import Order
from order.forms import OrderCreateForm

def order_create(request):
    context={}
    total_cost = 0
    form = OrderCreateForm()
    products_in_cart = ProductInCart.objects.all()
    if request.method == 'POST':
        if user.is_anonymous
            return render(request, 'orders/order_create.html',
                          context)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            customer = form.save()
            order=Order.objects.get_or_create(customer=customer)
            for product in products_in_cart:
                ProductInOrder.objects.get_or_create(customer=customer,
                                                     product=product,
                                                     total_price=product.total_price,
                                                     total_count=product.total_count)
                total_cost += product.total_price
                total_count += product.total_count
            product_in_order = ProductInOrder.objects.all()
            ProductInCart.objects.all().delete()
            context = {'product_in_order': product_in_order,
                       'total_cost': total_cost,
                       'total_count': total_count
                       'order': order,
                       'form': form
                       }
            return render(request, 'orders/order_created.html',
                      context)
    for product in products_in_cart:
        total_cost += product.total_price
        total_count += product.total_count
    context={'product_in_cart': product_in_cart,
             'total_cost': total_cost,
             'total_count': total_count
             'form': form
             }
    return render(request, 'orders/order_create.html',
                  context)