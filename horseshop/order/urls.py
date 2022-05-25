from django.urls import path

import order.views as order

app_name = 'order'

urlpatterns = [
    path('create/', order.create, name='create'),
    path('detail/', order.detail, name='detail'),
]
