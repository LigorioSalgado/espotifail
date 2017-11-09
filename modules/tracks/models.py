from django.db import models
import uuid
from modules.albums.models import Album
# Create your models here.


class Track(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    url_youtube = models.URLField()
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="tracks")
    raiting = models.DecimalField(
        max_digits=2, decimal_places=1, default=0.0)

    def __str__(self):
        return self.name
