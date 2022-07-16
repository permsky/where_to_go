from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Place


def get_place(request, place_id):
    place_obj = get_object_or_404(Place, id=int(place_id))
    images = list()
    for img in place_obj.images.all().order_by('precedence'):
        images.append(img.image.url)
    place = {
        'title': place_obj.title,
        'imgs': images,
        'description_short': place_obj.description_short,
        'description_long': place_obj.description_long,
        'coordinates': {
            'lat': place_obj.latitude,
            'lng': place_obj.longitude
        }
    }
    return JsonResponse(
        place,
        json_dumps_params={'ensure_ascii': False, 'indent': 4}
    )
