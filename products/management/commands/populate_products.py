# products/management/commands/populate_products.py

import random
from django.core.management.base import BaseCommand
from products.models import Product


class Command(BaseCommand):
    help = 'Populate Products with mock data'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', type=int, default=10, help='Number of products to add')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(count):
            image = f"https://picsum.photos/id/{i}/200/300"
            name = f"Product {i}"
            price = round(random.uniform(1, 1000), 2)
            producer = f"Producer {i}"
            Product.objects.create(image=image, name=name, price=price, producer=producer)
        self.stdout.write(self.style.SUCCESS(f'{count} mock products added successfully'))
