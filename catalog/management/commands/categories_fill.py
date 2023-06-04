from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        category_list = [
            {'category_name': 'Еда', 'description': 'Еда на все случаи жизни'},
            {'category_name': 'Одежда', 'description': 'Мужская и женская одежда'},
            {'category_name': 'Автомобили', 'description': 'Автомобили на все случаи жизни'},
            {'category_name': 'Напитки', 'description': 'Детские и взрослые'},
        ]

        Category.objects.all().delete()

        created_categories = []

        for categories in category_list:
            created_categories.append(
                Category(**categories)
            )

        Category.objects.bulk_create(created_categories)