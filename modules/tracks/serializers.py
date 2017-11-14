from rest_framework import serializers
from .models import Track
#from modules.albums.serializers import AlbumModelSerializer


class TrackModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = ('__all__')


class TrackAlbumSerializer(serializers.ModelSerializer):
    #album = AlbumModelSerializer(read_only=True)

    class Meta:
        model = Track
        fields = ('id', 'name', 'duration', 'url_youtube', 'album')
