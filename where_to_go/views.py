from django.shortcuts import render
from django.urls import reverse

from places.models import Place


def index(request):
    features = list()
    places = Place.objects.all()
    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse(
                    'place_json',
                    kwargs={'place_id': place.id}
                )
            }
        }
        features.append(feature)
    context = {
        "places_geojson": {
            "type": "FeatureCollection",
            "features": features
        }
    }
    return render(request, 'index.html', context=context)
