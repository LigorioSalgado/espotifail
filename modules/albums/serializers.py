from rest_framework import serializers
from .models import Album


class AlbumModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('__all__')
