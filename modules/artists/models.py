from django.db import models
import uuid
from modules.albums.models import Album
# Create your models here.

GENRES = (
    ('POP', 'Pop'),
    ('ROCK', 'Rock'),
    ('ELT', 'Electronic'),
    ('JAZZ', 'Jazz'),
    ('CLS', 'Classic'),
    ('LTN', 'Latino'),
    ('RAP', 'Rap'),
    ('R&B', 'R&B'),
    ('FLK', 'Folk'),
    ('OT', 'Other')

)


class Artist(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,)
    name = models.CharField(max_length=100)
    biography = models.TextField()
    photo = models.URLField()
    albums = models.ManyToManyField(Album, blank=True)
    is_band = models.BooleanField(default=False)
    primary_genre = models.CharField(max_length=100, choices=GENRES)

    def __str__(self):
        return self.name
