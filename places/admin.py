from django.contrib import admin

from .models import Place, PlaceImage


class ImageInline(admin.TabularInline):
    model = PlaceImage
    readonly_fields = ('get_preview',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description_short',
        'longitude',
        'latitude',
    ]
    inlines = [
        ImageInline,
    ]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = [
        'place',
        'image',
        'get_preview',
        'precedence',
    ]
    readonly_fields = ['get_preview']
