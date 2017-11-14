from rest_framework import serializers
from .models import Album
from modules.tracks.serializers import TrackModelSerializer


class AlbumModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('__all__')


class AlbumTracksSerializer(serializers.ModelSerializer):

    tracks = TrackModelSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'name', 'cover', 'track_count', 'genre', 'tracks')
