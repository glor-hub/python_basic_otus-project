from django.urls import path

import product.views as product

app_name = 'product'

urlpatterns = [
    path('detail/<int:pk>/', product.product_detail, name='detail'),
    path('list/<slug:subcategory_slug>/', product.product_list, name='list'),
    path('cart/detail/', product.cart_detail, name='cart_detail'),
    path('cart/add/item/<int:pk>/', product.cart_add_item, name='cart_add_item'),
    path('cart/reduce/item/<int:pk>/', product.cart_reduce_item, name='cart_reduce_item'),
    path('cart/detail/<int:pk>/',  product.cart_delete_item, name='cart_delete_item'),
]
