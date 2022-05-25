from django.urls import path

import order.views as order

app_name = 'order'

urlpatterns = [
    path('create/', order.order_create, name='create'),
    path('detail/', order.order_detail, name='detail'),
]
