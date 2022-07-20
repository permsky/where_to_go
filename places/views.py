from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Place


def get_place(request, place_id):
    place = get_object_or_404(Place, id=int(place_id))
    images = list()
    for img in place.images.all().order_by('precedence'):
        images.append(img.image.url)
    serialized_place = {
        'title': place.title,
        'imgs': images,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude
        }
    }
    return JsonResponse(
        serialized_place,
        json_dumps_params={'ensure_ascii': False, 'indent': 4}
    )
