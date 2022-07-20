import json
import os
from pathlib import Path
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, PlaceImage
from where_to_go.settings import BASE_DIR


class Command(BaseCommand):
    def handle(self, *args, **options):
        places_json_directory = os.path.join(BASE_DIR, 'place_examples')

        filepaths = Path(places_json_directory).rglob('*.json')
        for filepath in filepaths:
            with open(filepath, encoding='UTF-8', mode='r') as f:
                serialized_place = json.load(f)
            place, is_not_found = Place.objects.get_or_create(
                title=serialized_place['title'],
                defaults={
                    'description_short': serialized_place['description_short'],
                    'description_long': serialized_place['description_long'],
                    'longitude': serialized_place['coordinates']['lng'],
                    'latitude': serialized_place['coordinates']['lat']
                }
            )
            if not is_not_found:
                continue
            for number, img_url in enumerate(serialized_place['imgs']):
                response = requests.get(img_url)
                response.raise_for_status()
                parsed_url = urlparse(img_url)
                content = ContentFile(response.content)
                place_img, _ = PlaceImage.objects.get_or_create(
                    place=place,
                    precedence=number
                )
                place_img.image.save(
                    Path(parsed_url.path).name,
                    content,
                    save=True
                )
