import os

from django.core.management.base import BaseCommand

from places.utils import fill_database
from where_to_go.settings import BASE_DIR


class Command(BaseCommand):
    def handle(self, *args, **options):
        places_json_directory = os.path.join(BASE_DIR, 'place_examples')

        fill_database(places_json_directory)
