from django.shortcuts import render, get_object_or_404

from order.models import Order
from order.forms import OrderCreateForm

from product.models import ProductInOrder

from product.models import ProductInCart


def order_create(request):
    context = {}
    total_cost = 0
    total_count=0
    form = OrderCreateForm()
    products_in_cart = ProductInCart.objects.all()
    if request.method == 'POST':
        # if user.is_anonymous
        #     return render(request, 'orders/order_create.html',
        #                   context)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            customer = form.save()
            Order.objects.get_or_create(customer=customer)
            order =get_object_or_404(Order, customer=customer)
            for product in products_in_cart:
                ProductInOrder.objects.get_or_create(order=order,
                                                     product=product.product,
                                                     total_price=product.total_price,
                                                     total_count=product.total_count)
                total_cost += product.total_price
                total_count += product.total_count
            order.total_price=total_cost
            order.total_count = total_count
            order.save()
            ProductInCart.objects.all().delete()
            products_in_order = ProductInOrder.objects.filter(order=order)
            context = {'products_in_order': products_in_order,
                       'order': order,
                       'form': form
                       }
            return render(request, 'order/order_created.html',
                          context)
    for product in products_in_cart:
        total_cost += product.total_price
        total_count += product.total_count
    context = {'products_in_cart': products_in_cart,
               'total_cost': total_cost,
               'total_count': total_count,
               'form': form
               }
    return render(request, 'order/order_create.html',
                  context)


def order_detail(request):
    orders=Order.objects.all()
    products_in_order = ProductInOrder.objects.all()
    context = {'products_in_order': products_in_order,
               'orders': orders,
               }
    return render(request, 'order/order_detail.html',
                  context)
