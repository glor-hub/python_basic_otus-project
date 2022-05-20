from django.core.management.base import BaseCommand

from product.models import (
    Manufacturer,
    Product,
)

from category.models import (
    Subcategory,
)


class Command(BaseCommand):

    def handle(self, *args, **options):
        contacts = {'Eskadron': {'country': 'Germany',
                                 'phone': '+49 520 370 40',
                                 'email': 'info@pikeur.de'},
                    'Roeckl': {'country': 'Germany',
                               'phone': '+49 089 729 6958',
                               'email': 'kundenservice@roeckl.com'},
                    'Tommy Hilfiger': {'country': 'Switzerland',
                                       'phone': '810 800 866 694 45',
                                       'email': 'info:@globaltommy.com'},
                    'Amahorse': {'country': 'Italy',
                                 'phone': '+39 075 856 0191',
                                 'email': 'info@amahorse.com'}
                    }
        companies = [
            'Eskadron',
            'Roeckl',
            'Tommy Hilfiger',
            'Amahorse'
        ]

        for company in companies:
            Manufacturer.objects.get_or_create(name=company,
                                               country=contacts[company]["country"],
                                               phone=contacts[company]["phone"],
                                               email=contacts[company]["email"]
                                               )
        goods = {'saddle pad "COTTON" DR': {'price': 500,
                                            'count': 29,
                                            'subcategory': Subcategory(name='Saddle Pads'),
                                            'manufacturer': Manufacturer(name='Eskadron'),
                                            'property': ProductProperty()},
                 'gloves "TRYON"': {'price': 150,
                                    'count': 8,
                                    'subcategory': Subcategory(name='Riding Gloves'),
                                    'manufacturer': Manufacturer(name='Roeckl')},
                 'breeches "Performans"': {'price': 378,
                                           'count': 17,
                                           'subcategory': Subcategory(name='Breeches'),
                                           'manufacturer': Manufacturer(name='Tommy Hilfiger')},
                 'helmet "EQUESTRO FRAME"': {'price': 450,
                                             'count': 3,
                                             'subcategory': Subcategory(name='Helmets&Hats'),
                                             'manufacturer': Manufacturer(name='Amahorse')}
                 }
        products = [
            'saddle pad "COTTON" DR',
            'gloves "TRYON"',
            'breeches "Performans"',
            'helmet "EQUESTRO FRAME"'
        ]
        for product in products:
            Product.objects.get_or_create(name=product,
                                          curr_price=goods[product]["price"],
                                          curr_count=goods[product]["count"],
                                          subcategory=goods[product]["subcategory"],
                                          manufacturer=goods[product]["manufacturer"]
                                          )
