from django.db import models
from django.utils.html import format_html


class Place(models.Model):
    title = models.CharField('название места', max_length=250)
    description_short = models.TextField('краткое описание')
    description_long = models.TextField('подробное описание')
    longitude = models.FloatField('долгота')
    latitude = models.FloatField('широта')

    class Meta:
        verbose_name = 'Место куда пойти'
        verbose_name_plural = 'Места куда пойти'

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='фото места',
        related_name='images'
    )
    precedence = models.SmallIntegerField(
        'очередность отображения фото',
        default=0,
        db_index=True
    )
    image = models.ImageField('фото')

    class Meta:
        verbose_name = 'Фотография места'
        verbose_name_plural = 'Фотографии мест'
        ordering = ['precedence']

    def __str__(self):
        return f'{self.precedence} {self.place.title}'
    
    def get_preview(self):
        return format_html(
            '<img src="{url}" height=200 />',
            url = self.image.url
        )
