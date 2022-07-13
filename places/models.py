from django.db import models


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
        verbose_name='фото места'
    )
    precedence = models.SmallIntegerField('очередность отображения фото')
    image = models.ImageField('фото')

    class Meta:
        verbose_name = 'Фотография места'
        verbose_name_plural = 'Фотографии мест'

    def __str__(self):
        return f'{self.precedence} {self.place.title}'
