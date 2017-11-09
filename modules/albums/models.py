from django.db import models
import uuid
from django.conf import settings
# Create your models here.


class Album(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    cover = models.URLField()
    release_day = models.DateField()
    copyright = models.CharField(max_length=100)
    track_count = models.IntegerField()
    genre = models.CharField(max_length=100)
    country = models.CharField(max_length=100, choices=settings.COUNTRIES)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    currency = models.CharField(max_length=10)

    def __str__(self):
        return self.name
