from django.urls import path

import product.views as product

app_name = 'product'

urlpatterns = [
    path('detail/<int:pk>/', product.ProductDetailView.as_view(), name='detail'),
    path('list/<slug:subcategory_slug>/', product.product_list, name='list'),
]
