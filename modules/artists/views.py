from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Artist
from .serializers import ArtistsModelSerializer
from django.http import Http404

# Create your views here.


class ListArtist(APIView):
    '''
    Este endpoint trae todos los artistas
    '''

    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistsModelSerializer(artists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArtistsModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailArtist(APIView):

    def _get_artist(self, id):
        try:
            artist = Artist.objects.get(pk=id)
            return artist
        except Artist.DoesNotExist:
            raise Http404

    def get(self, request, id):
        artist = get_object_or_404(Artist, pk=id)
        serializer = ArtistsModelSerializer(artist)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        artist = self._get_artist(id)
        serializer = ArtistsModelSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        artist = self._get_artist(id)
        serializer = ArtistsModelSerializer(
            artist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        artist = self._get_artist(id)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
