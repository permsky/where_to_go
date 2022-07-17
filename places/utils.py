import json
from pathlib import Path
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.db.utils import IntegrityError

from places.models import Place, PlaceImage


def read_from_json(filepath):
    with open(filepath, encoding='UTF-8', mode='r') as f:
        return json.loads(f.read())


def fill_database(directory):
    filepaths = Path(directory).rglob('*.json')
    for filepath in filepaths:
        try:
            place = read_from_json(str(filepath))
            place_obj, _ = Place.objects.get_or_create(
                title=place['title'],
                description_short=place['description_short'],
                description_long=place['description_long'],
                longitude=place['coordinates']['lng'],
                latitude=place['coordinates']['lat']
            )
            for img_url in place['imgs']:
                response = requests.get(img_url)
                response.raise_for_status()
                parsed_url = urlparse(img_url)
                content = ContentFile(response.content)
                place_img, _ = PlaceImage.objects.get_or_create(
                    place=place_obj
                )
                place_img.image.save(
                    Path(parsed_url.path).name,
                    content,
                    save=True
                )
        except IntegrityError:
            continue
