from django.contrib import admin

from .models import Product, ProductInOrder,Manufacturer, ProductProperty, ProductInCart

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductInOrder)
admin.site.register(ProductInCart)
admin.site.register(Manufacturer)
admin.site.register(ProductProperty)
