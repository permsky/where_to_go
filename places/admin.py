from django.contrib import admin

from .models import Place, PlaceImage


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description_short',
        'longitude',
        'latitude',
    ]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = [
        'place',
        'precedence',
        'image',
    ]
