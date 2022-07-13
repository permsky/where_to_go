from django.shortcuts import render

from places.models import Place


def index(request):
    features = list()
    for place in Place.objects.all():
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": f"/static/places/{place.id}.json"
            }
        }
        features.append(feature)
    context = {
        "places_geojson":
        {
            "type": "FeatureCollection",
            "features": features
        }
    }
    return render(request, 'index.html', context=context)
