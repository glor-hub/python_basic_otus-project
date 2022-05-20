from django.core.management.base import BaseCommand

from category.models import (
    Category,
    Subcategory,
)


class Command(BaseCommand):

    def handle(self, *args, **options):
        subcategories = {'For Rider': ['Riding Gloves',
                                       'Breeches',
                                       'Riding Boots',
                                       'Helmets&Hats',
                                       'Whips'],  # Хлысты
                         'For Horse': ['Saddles',  # Седла
                                       'Saddle Pads',  # Вальтрапы
                                       'Bridles',  # Уздечки
                                       'Stirrups'  # Стремена
                                       ]
                         }
        categories = [
            'For Rider',
            'For Horse'
        ]
        for category in categories:
            categ=Category.objects.get(name=category)
            for subcategory in subcategories[category]:
                Subcategory.objects.get_or_create(name=subcategory,
                                                  category=categ)
