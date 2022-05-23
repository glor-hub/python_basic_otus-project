from django.urls import path

import product.views as product

app_name = 'product'

urlpatterns = [
    path('detail/<int:pk>/', product.product_detail, name='detail'),
    path('list/<slug:subcategory_slug>/', product.product_list, name='list'),
    # path('add/<int:pk>/', product.product_add_to_cart, name='product_add_to_cart'),
    path('cart/detail/<int:pk>/', product.cart_detail, name='cart_detail'),

]
