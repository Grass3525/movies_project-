from django.contrib.auth import get_user_model
from django.db import models

USER = get_user_model()

__all__ = ["Movie", "StreamingChannel"]


class StreamingChannel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    owner = models.ForeignKey(
        USER,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=250)
    subtitle = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )
    director = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    channels = models.ManyToManyField(
        StreamingChannel,
        related_name='movies',
        blank=True,
    )

    def __str__(self):
        return self.title
