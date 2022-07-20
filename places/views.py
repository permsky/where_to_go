from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Place


def get_place(request, place_id):
    place = get_object_or_404(Place, id=int(place_id))
    place_images = place.images.all().order_by('precedence')
    images = [img.image.url for img in place_images]
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
