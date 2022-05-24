from django.urls import path

import product.views as product

app_name = 'product'

urlpatterns = [
    path('detail/<int:pk>/', product.product_detail, name='detail'),
    path('list/<slug:subcategory_slug>/', product.product_list, name='list'),
    path('cart/detail/', product.cart_detail, name='cart_detail'),

]
