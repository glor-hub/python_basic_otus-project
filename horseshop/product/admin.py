from django.contrib import admin

from .models import Product, ProductInOrder, Manufacturer, ProductInCart

admin.site.register(Product)
admin.site.register(ProductInOrder)
admin.site.register(ProductInCart)
admin.site.register(Manufacturer)
