from django.core.management.base import BaseCommand

from category.models import (
    Category,
)


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = [
            'For Rider',
            'For Horse'
        ]
        for category in categories:
            Category.objects.get_or_create(name=category)
