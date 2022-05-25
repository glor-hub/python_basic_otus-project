from django.views.generic import ListView
from order.models import Order

class OrderListView(ListView):
    model = Order
