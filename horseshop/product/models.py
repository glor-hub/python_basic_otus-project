from django.db import models
from django.db.models.signals import post_save

# Create your models here.
from category.models import Subcategory
from order.models import Order


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    email = models.EmailField()
    site = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} {self.country}"


class ProductProperty(models.Model):
    BLACK = 'BK'
    WHITE = 'WT'
    BLUE = 'BL'
    BROWN = 'BR'
    RED = 'RD'
    GREEN = 'GR'

    COLORS = [
        (BLACK, 'Black'),
        (WHITE, 'White'),
        (BLUE, 'Blue'),
        (BROWN, 'Brown'),
        (RED, 'Red'),
        (GREEN, 'Green')
    ]
    CHILD = 'C'
    MALE = 'M'
    FEMALE = 'F'
    GENDER = [
        (CHILD, 'Child'),
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]
    SIZES = [(38, '38'),
             (40, '40'),
             (42, '42'),
             (44, '44'),
             (46, '46'),
             (120, '120'),
             (130, '130'),
             (140, '140'),
             (150, '150'),
             (160, '160'),
             ]
    color = models.CharField(max_length=2, choices=COLORS, default='BK')
    size = models.PositiveIntegerField(choices=SIZES, default=38)
    gender = models.CharField(max_length=1, choices=GENDER, default='M')

    def __str__(self):
        return f"color:{self.color}, size:{self.size}, gender:{self.gender}"


class Product(models.Model):
    name = models.CharField(max_length=64)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
    curr_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    curr_count = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)
    property = models.ForeignKey(ProductProperty, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_count = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        price_per_item = self.product.curr_price
        self.price_per_item = price_per_item
        self.total_price = self.total_count * self.price_per_item
        super().save(*args, **kwargs)

    def __str__(self):
        return f"product {self.product.name} in order {self.order.pk}"

def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    order_total_count = 0

    for item in all_products_in_order:
        order_total_price += item.total_price
        order_total_count += item.total_count

    instance.order.total_price = order_total_price
    instance.order.total_count = order_total_count

    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)

class ProductInCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_count = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        price_per_item = self.product.curr_price
        self.price_per_item = price_per_item
        self.total_price = self.total_count * self.price_per_item
        super().save(*args, **kwargs)

    def __str__(self):
        return f"product {self.product.name}"
