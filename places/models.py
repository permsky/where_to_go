from email.policy import default
from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('название места', unique=True, max_length=250)
    description_short = models.TextField('краткое описание', unique=True)
    description_long = HTMLField('длинное описание', unique=True)
    longitude = models.FloatField('долгота')
    latitude = models.FloatField('широта')

    class Meta:
        verbose_name = 'Место куда пойти'
        verbose_name_plural = 'Места куда пойти'
        unique_together = ['longitude', 'latitude']

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
    image = models.ImageField('фото', default='default.jpg')

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
