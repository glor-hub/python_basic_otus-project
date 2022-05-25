from django.urls import path

import order.views as order

app_name = 'order'

urlpatterns = [
    path('', order.OrderListView.as_view(), name='list'),

]
