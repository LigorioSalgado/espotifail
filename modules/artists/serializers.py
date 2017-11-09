from rest_framework import serializers
from .models import Artist

# class ArtistsSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     biography = serializers.CharField(max_length=500)


class ArtistsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        #fields = ('id', 'name', 'biography', 'photo', 'albums', 'is_band')
        fields = ('__all__')
        #exclude = ('primary_genre',)
