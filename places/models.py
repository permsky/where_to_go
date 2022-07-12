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
