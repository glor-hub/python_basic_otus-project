from django.core.management.base import BaseCommand

from product.models import (
    Product,
    Manufacturer,
)
from category.models import (
    Subcategory,
)



class Command(BaseCommand):

    def handle(self, *args, **options):

        goods = {'saddle pad "COTTON" DR': {'price': 500,
                                            'count': 29,
                                            'manufacturer': Manufacturer(id=1),
                                            'subcategory': Subcategory(id=16)},
                 'gloves "TRYON"': {'price': 150,
                                    'count': 8,
                                    'manufacturer': Manufacturer(id=2),
                                    'subcategory': Subcategory(id=11)},
                 'breeches "Performans"': {'price': 378,
                                           'count': 17,
                                           'manufacturer': Manufacturer(id=3),
                                           'subcategory': Subcategory(id=12)},
                 'Roeckl Lona Riding gloves': {'price': 174,
                                           'count': 9,
                                           'manufacturer': Manufacturer(id=2),
                                           'subcategory': Subcategory(id=11)},
                 'helmet "EQUESTRO FRAME"': {'price': 450,
                                             'count': 3,
                                             'manufacturer': Manufacturer(id=4),
                                             'subcategory': Subcategory(id=14)}
                 }
        products = [
            'saddle pad "COTTON" DR',
            'gloves "TRYON"',
            'breeches "Performans"',
            'helmet "EQUESTRO FRAME"',
            'Roeckl Lona Riding gloves'
        ]
        for product in products:
            Product.objects.get_or_create(name=product,
                                          curr_price=goods[product]["price"],
                                          curr_count=goods[product]["count"],
                                          manufacturer=goods[product]["manufacturer"],
                                          subcategory=goods[product]["subcategory"]
                                          )
